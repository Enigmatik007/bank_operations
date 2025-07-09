"""Тесты для модуля utils."""

from unittest.mock import mock_open, patch

from src.utils import load_transactions


def test_load_valid_transactions() -> None:
    """Тестирует загрузку валидного файла с транзакциями."""
    test_data = '[{"id": 1, "state": "EXECUTED"}]'
    with patch('builtins.open', mock_open(read_data=test_data)):
        result = load_transactions('valid.json')
        assert result == [{'id': 1, 'state': 'EXECUTED'}]


def test_load_empty_file() -> None:
    """Тестирует загрузку пустого файла."""
    with patch('builtins.open', mock_open(read_data='')):
        assert load_transactions('empty.json') == []


def test_file_not_found() -> None:
    """Тестирует обработку отсутствующего файла."""
    with patch('builtins.open', side_effect=FileNotFoundError):
        assert load_transactions('missing.json') == []


def test_invalid_json_format() -> None:
    """Тестирует обработку невалидного JSON."""
    test_data = 'invalid json'
    with patch('builtins.open', mock_open(read_data=test_data)):
        assert load_transactions('invalid.json') == []


def test_not_list_data() -> None:
    """Тестирует обработку JSON, который не является списком."""
    test_data = '{"id": 1, "state": "EXECUTED"}'
    with patch('builtins.open', mock_open(read_data=test_data)):
        assert load_transactions('not_list.json') == []


def test_unexpected_error() -> None:
    """Тестирует обработку непредвиденных ошибок."""
    with patch('builtins.open', side_effect=Exception("Unexpected error")):
        assert load_transactions('error.json') == []
