"""Модуль для чтения CSV и Excel файлов с транзакциями.

Этот модуль содержит функции для чтения данных транзакций из файлов форматов CSV и Excel.
Данные возвращаются в виде списка словарей с ключами-строками и значениями произвольного типа.

Функции:
- read_csv_file(file_path): читает CSV файл с разделителем ';' и возвращает список транзакций.
- read_excel_file(file_path): читает Excel файл (xlsx) и возвращает список транзакций.

Ошибки при чтении логируются, в случае ошибки возвращается пустой список.
"""

from pathlib import Path
from typing import Any, Dict, List, Union, cast

import pandas as pd

from .log_config import setup_logger

logger = setup_logger(__name__, "logs/file_handlers.log")


def read_csv_file(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Читает транзакции из CSV файла.

    Args:
        file_path (Union[str, Path]): Путь к CSV файлу. Может быть строкой или объектом Path.

    Returns:
        List[Dict[str, Any]]: Список словарей, где каждый словарь соответствует одной записи (транзакции).
                             Ключи словарей — строки, значения — данные из файла.

    Raises:
        В случае ошибки чтения файла, ошибка логируется, и возвращается пустой список.
    """
    try:
        df = pd.read_csv(file_path, delimiter=';')
        # Явно приводим тип для подавления предупреждений PyCharm
        return cast(List[Dict[str, Any]], df.to_dict("records"))
    except Exception as e:
        logger.error(f"Ошибка чтения CSV: {e}")
        return []


def read_excel_file(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Читает транзакции из Excel файла.

    Args:
        file_path (Union[str, Path]): Путь к Excel файлу. Может быть строкой или объектом Path.

    Returns:
        List[Dict[str, Any]]: Список словарей, где каждый словарь соответствует одной записи (транзакции).
                             Ключи словарей — строки, значения — данные из файла.

    Raises:
        В случае ошибки чтения файла, ошибка логируется, и возвращается пустой список.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        return cast(List[Dict[str, Any]], df.to_dict("records"))
    except Exception as e:
        logger.error(f"Ошибка чтения Excel: {e}")
        return []
