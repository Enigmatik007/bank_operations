"""Модуль для работы с транзакциями.

Содержит функции для загрузки данных из JSON-файлов.
"""

import json
import logging
from typing import Any, Dict, List
from src.log_config import setup_logger

logger = setup_logger(__name__, "logs/utils.log")

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла.

    Args:
        file_path: Путь к JSON-файлу с транзакциями.

    Returns:
        Список словарей с транзакциями. Возвращает пустой список при:
        - Отсутствии файла
        - Ошибках формата JSON
        - Некорректном формате данных

    Examples:
        >>> load_transactions("operations.json")
        [{"id": 441945886, "state": "EXECUTED"}]
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if not isinstance(data, list):
                logger.warning("Файл %s не содержит список", file_path)
                return []

            return data

    except FileNotFoundError:
        logger.error("Файл не найден: %s", file_path)
        return []
    except json.JSONDecodeError as e:
        logger.error("Ошибка JSON в %s: %s", file_path, str(e))
        return []
