import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions

# Тестовые данные
TEST_JSON_DATA = """
[
    {"id": 441945886, "state": "EXECUTED"},
    {"id": 41428829, "state": "CANCELED"}
]
"""

@patch("builtins.open", new_callable=mock_open, read_data=TEST_JSON_DATA)
def test_load_transactions_valid_file(mock_file):
    """Тест загрузки корректного JSON-файла."""
    result = load_transactions("dummy_path.json")
    assert len(result) == 2
    assert result[0]["id"] == 441945886
    mock_file.assert_called_with("dummy_path.json", "r", encoding="utf-8")

@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_transactions_file_not_found(mock_file):
    """Тест обработки отсутствующего файла."""
    result = load_transactions("missing.json")
    assert result == []

@patch("builtins.open", new_callable=mock_open, read_data="{}")
def test_load_transactions_invalid_json(mock_file):
    """Тест загрузки некорректного JSON (не список)."""
    result = load_transactions("invalid.json")
    assert result == []

@patch("builtins.open", new_callable=mock_open, read_data="not a json")
def test_load_transactions_malformed_json(mock_file):
    """Тест обработки битого JSON."""
    result = load_transactions("malformed.json")
    assert result == []

def test_load_transactions_empty_file(tmp_path):
    """Тест пустого файла через временную директорию."""
    file_path = tmp_path / "empty.json"
    file_path.write_text("")
    assert load_transactions(file_path) == []
