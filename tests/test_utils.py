"""Тесты для модуля utils.py.

Проверяют загрузку транзакций из файлов.
"""

from typing import Any
from unittest.mock import mock_open, patch
import pytest
from src.utils import load_transactions

def test_load_transactions_valid_file() -> None:
    """Тестирует загрузку корректного файла."""
    test_data = '[{"id": 1, "state": "EXECUTED"}]'
    with patch("builtins.open", mock_open(read_data=test_data)):
        result = load_transactions("valid.json")
        assert result == [{"id": 1, "state": "EXECUTED"}]

def test_load_transactions_empty_list() -> None:
    """Тестирует загрузку файла с пустым списком."""
    with patch("builtins.open", mock_open(read_data="[]")):
        assert load_transactions("empty.json") == []

def test_load_transactions_invalid_json() -> None:
    """Тестирует обработку битого JSON."""
    with patch("builtins.open", mock_open(read_data="{")):
        assert load_transactions("broken.json") == []

def test_load_transactions_file_not_found() -> None:
    """Тестирует обработку отсутствующего файла."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert load_transactions("missing.json") == []
