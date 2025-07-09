"""Тесты для модуля file_handlers."""

from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import MagicMock, patch

import pytest

from src.file_handlers import read_csv_file, read_excel_file


@patch("pandas.read_csv")
def test_read_csv_success(mock_read: MagicMock) -> None:
    """Тестирует успешное чтение CSV файла.

    Args:
        mock_read: Мок для pandas.read_csv
    """
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read.return_value = mock_df

    result = read_csv_file(Path("data/transactions.csv"))
    assert result == [{"id": 1, "amount": 100}]


@patch("pandas.read_excel")
def test_read_excel_success(mock_read: MagicMock) -> None:
    """Тестирует успешное чтение Excel файла.

    Args:
        mock_read: Мок для pandas.read_excel
    """
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]
    mock_read.return_value = mock_df

    result = read_excel_file(Path("data/transactions_excel.xlsx"))
    assert result == [{"id": 2, "amount": 200}]
