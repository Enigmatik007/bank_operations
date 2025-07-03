"""Модуль для маскирования банковских реквизитов."""

from .log_config import setup_logger

logger = setup_logger(__name__, 'logs/masks.log')


def _validate_number(number: str, required_length: int, name: str) -> None:
    """Валидирует номер карты или счета.

    Args:
        number (str): Номер для проверки
        required_length (int): Минимальная длина
        name (str): Тип номера ('карты' или 'счета')

    Raises:
        ValueError: При невалидном номере
    """
    if not isinstance(number, str) or not number.isdigit():
        error_msg = f'Номер {name} должен содержать только цифры'
        logger.error(error_msg)
        raise ValueError(error_msg)

    if len(number) < required_length:
        error_msg = f'Номер {name} должен содержать минимум {required_length} цифр'
        logger.error(error_msg)
        raise ValueError(error_msg)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты.

    Args:
        card_number (str): 16-значный номер карты

    Returns:
        str: Маскированный номер формата "XXXX XX** **** XXXX"
    """
    _validate_number(card_number, 16, 'карты')
    return f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета.

    Args:
        account_number (str): Номер счета

    Returns:
        str: Маскированный номер формата "**XXXX"
    """
    _validate_number(account_number, 4, 'счета')
    return f'**{account_number[-4:]}'
