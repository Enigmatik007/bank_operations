"""Модуль для чтения финансовых операций из CSV и Excel."""

from typing import List, Dict, Any
import pandas as pd
from pathlib import Path
from .log_config import setup_logger

logger = setup_logger(__name__, "logs/file_handlers.log")


def read_csv_file(file_path: str | Path) -> List[Dict[str, Any]]:
    """Читает транзакции из CSV.

    Args:
        file_path (str | Path): Путь к CSV-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибке.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка чтения CSV {file_path}: {e}")
        return []


def read_excel_file(file_path: str | Path) -> List[Dict[str, Any]]:
    """Читает транзакции из Excel.

    Args:
        file_path (str | Path): Путь к XLSX-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибке.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        return df.to_dict("records")
    except Exception as e:
        logger.error(f"Ошибка чтения Excel {file_path}: {e}")
        return []