"""Модуль для чтения CSV и Excel файлов с транзакциями."""

from pathlib import Path
from typing import Any, Dict, List, Union

import pandas as pd

from .log_config import setup_logger

logger = setup_logger(__name__, "logs/file_handlers.log")


def read_csv_file(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Читает транзакции из CSV файла."""
    try:
        df = pd.read_csv(file_path, delimiter=';')
        return [dict(row) for row in df.to_dict("records")]  # Явное преобразование
    except Exception as e:
        logger.error(f"Ошибка чтения CSV: {e}")
        return []


def read_excel_file(file_path: Union[str, Path]) -> List[Dict[str, Any]]:
    """Читает транзакции из Excel файла."""
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        return [dict(row) for row in df.to_dict("records")]  # Явное преобразование
    except Exception as e:
        logger.error(f"Ошибка чтения Excel: {e}")
        return []
