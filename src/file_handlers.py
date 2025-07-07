"""Модуль для чтения CSV и Excel файлов с транзакциями."""

from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from .log_config import setup_logger

logger = setup_logger(__name__, "logs/file_handlers.log")


def read_csv_file(file_path: str | Path) -> List[Dict[str, Any]]:
    """Читает транзакции из CSV.

    Args:
        file_path: Путь к CSV-файлу.

    Returns:
        Список словарей с данными транзакций.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка чтения CSV: {e}")
        return []


def read_excel_file(file_path: str | Path) -> List[Dict[str, Any]]:
    """Читает транзакции из Excel.

    Args:
        file_path: Путь к Excel-файлу (.xlsx).

    Returns:
        Список словарей с данными транзакций.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        return df.to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка чтения Excel: {e}")
        return []
