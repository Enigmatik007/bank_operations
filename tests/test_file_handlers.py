import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.file_handlers import read_csv_file, read_excel_file

@patch("pandas.read_csv")
def test_read_csv_success(mock_read):
    """Тест успешного чтения CSV."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read.return_value = mock_df

    result = read_csv_file("test.csv")
    assert result == [{"id": 1, "amount": 100}]

@patch("pandas.read_excel")
def test_read_excel_success(mock_read):
    """Тест успешного чтения Excel."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]
    mock_read.return_value = mock_df

    result = read_excel_file("test.xlsx")
    assert result == [{"id": 2, "amount": 200}]

def test_read_csv_invalid_path():
    """Тест ошибки при неверном пути."""
    result = read_csv_file("nonexistent.csv")
    assert result == []

def test_read_excel_invalid_path():
    """Тест ошибки при неверном пути."""
    result = read_excel_file("nonexistent.xlsx")
    assert result == []