import os
from typing import Generator
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import convert_to_rub


@pytest.fixture
def mock_api() -> Generator[Mock, None, None]:
    """
    Фикстура для мокирования API запросов.
    """
    with patch('src.external_api.requests.get') as mock_get:
        yield mock_get


def test_convert_rub_no_conversion() -> None:
    """
    Тест конвертации RUB в RUB (без реальной конвертации).
    """
    transaction = {'operationAmount': {'amount': '500.00', 'currency': {'code': 'RUB'}}}
    assert convert_to_rub(transaction) == 500.00


def test_convert_usd_to_rub(mock_api: Mock) -> None:
    """
    Тест конвертации USD в RUB с мокированным API.
    """
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.50}}
    mock_response.raise_for_status.return_value = None
    mock_api.return_value = mock_response

    with patch('src.external_api.API_KEY', 'test_key'):
        transaction = {'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}}
        assert convert_to_rub(transaction) == 7550.00


def test_convert_invalid_amount(mock_api: Mock) -> None:
    """
    Тест обработки невалидной суммы.
    """
    transaction = {'operationAmount': {'amount': 'invalid', 'currency': {'code': 'USD'}}}
    assert convert_to_rub(transaction) is None


def test_convert_api_error(mock_api: Mock) -> None:
    """
    Тест обработки ошибки API.
    """
    mock_api.side_effect = requests.RequestException("API error")
    transaction = {'operationAmount': {'amount': '100.00', 'currency': {'code': 'USD'}}}
    assert convert_to_rub(transaction) is None


def test_convert_missing_api_key() -> None:
    """
    Тест отсутствия API ключа.
    """
    transaction = {'operationAmount': {'amount': '100.00', 'currency': {'code': 'EUR'}}}
    with patch('src.external_api.API_KEY', None):
        assert convert_to_rub(transaction) is None


def test_real_api_conversion() -> None:
    """
    Тест реального API (автоматически пропускается если API недоступен).
    """
    try:
        if not os.getenv('EXCHANGE_RATE_API_KEY'):
            pytest.skip("API ключ не найден в .env")

        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/latest",
            headers={'apikey': os.getenv('EXCHANGE_RATE_API_KEY')},
            timeout=5,
        )
        if response.status_code != 200:
            pytest.skip("API недоступен")
    except requests.RequestException:
        pytest.skip("Ошибка соединения с API")

    transaction = {'operationAmount': {'amount': '1.00', 'currency': {'code': 'USD'}}}
    result = convert_to_rub(transaction)
    assert isinstance(result, float)
    assert result > 0
