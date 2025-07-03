"""Модуль конфигурации логгеров для банковских операций."""

import logging


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """Инициализирует и настраивает логгер.

    Args:
        name (str): Имя логгера (обычно __name__)
        log_file (str): Путь к файлу логов

    Returns:
        logging.Logger: Настроенный объект логгера
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(filename=log_file, mode='w', encoding='utf-8')

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
