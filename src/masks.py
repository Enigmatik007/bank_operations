"""Модуль для маскирования банковских реквизитов.

Содержит функции для валидации и форматирования номеров карт и счетов.
"""

import logging
from src.log_config import setup_logger

logger = setup_logger(__name__, "logs/masks.log")

def _validate_number(number: str, required_length: int, name: str) -> None:
    """Проверяет корректность номера карты или счета.

    Args:
        number: Номер для проверки (только цифры).
        required_length: Минимально допустимая длина номера.
        name: Тип номера ('карты' или 'счета') для сообщения об ошибке.

    Raises:
        ValueError: Если номер:
            - Не является строкой
            - Содержит нецифровые символы
            - Короче required_length

    Examples:
        >>> _validate_number("12345678", 8, "карты")  # Валидный номер
        >>> _validate_number("123abc", 8, "счета")    # ValueError
    """
    if not isinstance(number, str) or not number.isdigit():
        error_msg = f"Номер {name} должен содержать только цифры"
        logger.error(error_msg)
        raise ValueError(error_msg)

    if len(number) < required_length:
        error_msg = f"Номер {name} должен содержать минимум {required_length} цифр"
        logger.error(error_msg)
        raise ValueError(error_msg)

    logger.debug(f"Валидация номера {name} успешна")

def get_mask_card_number(card_number: str) -> str:
    """Генерирует маскированный номер карты.

    Args:
        card_number: 16-значный номер карты без пробелов.

    Returns:
        Отформатированная строка вида "XXXX XX** **** XXXX".

    Raises:
        ValueError: Если номер карты некорректен.

    Examples:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    _validate_number(card_number, 16, "карты")
    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Сгенерирована маска карты: {masked}")
    return masked

def get_mask_account(account_number: str) -> str:
    """Генерирует маскированный номер счета.

    Args:
        account_number: Номер счета (минимум 4 цифры).

    Returns:
        Отформатированная строка вида "**XXXX".

    Raises:
        ValueError: Если номер счета некорректен.

    Examples:
        >>> get_mask_account("73654108430135874305")
        '**4305'
    """
    _validate_number(account_number, 4, "счета")
    masked = f"**{account_number[-4:]}"
    logger.info(f"Сгенерирована маска счета: {masked}")
    return masked
