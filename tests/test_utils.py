"""Модуль тестирования функций загрузки транзакций."""

from pathlib import Path
from typing import Any, Dict, List
from unittest.mock import mock_open

import pytest

from src.utils import load_transactions


def test_load_valid_transactions(mocker: Any) -> None:
    """Тестирует загрузку корректного JSON-файла с транзакциями.

    Args:
        mocker: Фикстура для мокирования.
    """
    test_data = '[{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}]'
    mocker.patch("builtins.open", mock_open(read_data=test_data))
    result = load_transactions('valid.json')
    assert result == [{'id': 1, 'state': 'EXECUTED'}, {'id': 2, 'state': 'PENDING'}]


def test_load_empty_file(mocker: Any) -> None:
    """Тестирует обработку пустого файла.

    Args:
        mocker: Фикстура для мокирования.
    """
    mocker.patch("builtins.open", mock_open(read_data=''))
    result = load_transactions('empty.json')
    assert result == []


def test_file_not_found(mocker: Any) -> None:
    """Тестирует обработку отсутствующего файла.

    Args:
        mocker: Фикстура для мокирования.
    """
    mocker.patch("builtins.open", side_effect=FileNotFoundError)
    mocker.patch("src.decorators._write_log")
    result = load_transactions('missing.json')
    assert result == []


def test_invalid_json_format(mocker: Any) -> None:
    """Тестирует обработку некорректного JSON.

    Args:
        mocker: Фикстура для мокирования.
    """
    mocker.patch("builtins.open", mock_open(read_data='{invalid json}'))
    mocker.patch("src.decorators._write_log")
    result = load_transactions('invalid.json')
    assert result == []


def test_not_list_data(mocker: Any) -> None:
    """Тестирует обработку JSON-объекта вместо массива.

    Args:
        mocker: Фикстура для мокирования.
    """
    mocker.patch("builtins.open", mock_open(read_data='{"id": 1}'))
    result = load_transactions('not_list.json')
    assert result == []


def test_unexpected_error(mocker: Any) -> None:
    """Тестирует обработку непредвиденных ошибок.

    Args:
        mocker: Фикстура для мокирования.
    """
    mocker.patch("builtins.open", side_effect=Exception("DB error"))
    mocker.patch("src.decorators._write_log")
    result = load_transactions('error.json')
    assert result == []
