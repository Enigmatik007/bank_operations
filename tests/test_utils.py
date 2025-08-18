"""
Модуль тестов для функции load_transactions из src.utils.

Проверяет загрузку транзакций из файлов JSON, CSV и Excel с использованием моков.
"""

import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


def test_load_transactions_json(mocker):
    """
    Тест загрузки транзакций из JSON файла.
    Проверяет, что функция корректно парсит список транзакций.
    """
    test_data = '[{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}]'
    # Мокаем и exists, и open
    mocker.patch("pathlib.Path.exists", return_value=True)
    mocker.patch("src.utils.open", mock_open(read_data=test_data))
    result = load_transactions("dummy.json")
    assert result == [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}]


def test_load_transactions_csv(mocker):
    """
    Тест загрузки транзакций из CSV файла.
    Проверяет, что функция корректно читает CSV с заголовками.
    """
    test_data = "id,state\n1,EXECUTED\n2,PENDING\n"
    mocker.patch("pathlib.Path.exists", return_value=True)
    mocker.patch("src.utils.open", mock_open(read_data=test_data))
    result = load_transactions("dummy.csv")
    assert result == [{"id": "1", "state": "EXECUTED"}, {"id": "2", "state": "PENDING"}]


def test_load_transactions_excel(mocker):
    """
    Тест загрузки транзакций из Excel файла.
    Использует мок pandas.read_excel для возврата заранее подготовленных данных.
    """
    import pandas as pd

    # Подготовка тестового DataFrame
    df_mock = pd.DataFrame([
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "PENDING"}
    ])

    # Мокаем pd.read_excel и exists
    mocker.patch("pathlib.Path.exists", return_value=True)
    mocker.patch("src.utils.pd.read_excel", return_value=df_mock)

    result = load_transactions("dummy.xlsx")
    assert result == [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}]


def test_load_transactions_unsupported_extension(mocker):
    """
    Тест загрузки файла с неподдерживаемым расширением.
    Проверяет, что вызывается ValueError.
    """
    # 1. Мокаем exists() чтобы файл "существовал"
    mocker.patch("pathlib.Path.exists", return_value=True)

    # 2. Мокаем open() чтобы избежать реального открытия файла
    mocker.patch("builtins.open", mock_open())

    with pytest.raises(ValueError, match=f"Неизвестный формат файла: .unsupported"):
        load_transactions("file.unsupported")


def test_load_transactions_file_not_found():
    """
    Тест загрузки несуществующего файла.
    Проверяет, что вызывается FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        load_transactions("no_such_file.json")
