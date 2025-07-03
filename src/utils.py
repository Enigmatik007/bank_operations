"""Модуль для загрузки и обработки банковских транзакций."""

import json
from typing import Any, Dict, List

from .log_config import setup_logger

logger = setup_logger(__name__, 'logs/utils.log')


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибках

    Raises:
        Логирует ошибки, но не пробрасывает исключения
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if not isinstance(data, list):
                logger.warning('Файл %s не содержит список', file_path)
                return []

            return data

    except FileNotFoundError:
        logger.error('Файл не найден: %s', file_path)
        return []
    except json.JSONDecodeError as e:
        logger.error('Ошибка JSON в %s: %s', file_path, str(e))
        return []
    except Exception as e:
        logger.critical('Непредвиденная ошибка: %s', str(e))
        return []
