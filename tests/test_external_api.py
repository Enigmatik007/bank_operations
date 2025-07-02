import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub
import requests
import os


@pytest.fixture
def mock_api():
    with patch('src.external_api.requests.get') as mock_get:
        yield mock_get


def test_convert_rub_no_conversion():
    transaction = {
        'operationAmount': {
            'amount': '500.00',
            'currency': {'code': 'RUB'}
        }
    }
    assert convert_to_rub(transaction) == 500.00


def test_convert_usd_to_rub(mock_api):
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.50}}
    mock_response.raise_for_status.return_value = None
    mock_api.return_value = mock_response

    with patch('src.external_api.API_KEY', 'test_key'):
        transaction = {
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        }
        assert convert_to_rub(transaction) == 7550.00


def test_real_api_conversion():
    """Тест реального API (автоматически пропускается если API недоступен)"""
    # Проверяем доступность API
    try:
        if not os.getenv('EXCHANGE_RATE_API_KEY'):
            pytest.skip("API ключ не найден в .env")

        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/latest",
            headers={'apikey': os.getenv('EXCHANGE_RATE_API_KEY')},
            timeout=5
        )
        if response.status_code != 200:
            pytest.skip("API недоступен")
    except requests.RequestException:
        pytest.skip("Ошибка соединения с API")

    # Если API доступен - выполняем тест
    transaction = {
        'operationAmount': {
            'amount': '1.00',
            'currency': {'code': 'USD'}
        }
    }
    result = convert_to_rub(transaction)
    assert isinstance(result, float)
    assert result > 0
