# utils.py
import json
import logging
from typing import Any, Dict, List

# Настройка логера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создаем файловый обработчик (перезаписывает файл при каждом запуске)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Форматируем логи
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)

# Добавляем обработчик к логеру
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON-файла с логированием.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
                return data
            logger.warning(f"Файл {file_path} не содержит список транзакций")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
