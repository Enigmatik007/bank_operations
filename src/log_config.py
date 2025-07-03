# log_config.py
import logging


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """Настраивает и возвращает логгер с заданными параметрами.

    Args:
        name: Имя логгера (обычно __name__)
        log_file: Путь к файлу логов

    Returns:
        Настроенный объект логгера
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(filename=log_file, mode='w', encoding='utf-8')

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Предотвращаем дублирование логов
    logger.propagate = False

    return logger
