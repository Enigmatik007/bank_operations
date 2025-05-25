from datetime import datetime
from .masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты/счета в переданной строке.

    Примеры:
    >>> mask_account_card("Visa Platinum 7000792289606361")
    'Visa Platinum 7000 79** **** 6361'
    >>> mask_account_card("Счет 73654108430135874305")
    'Счет **4305'

    Args:
        data: Строка формата "Тип Номер" (например, "Visa Platinum 7000792289606361")
    Returns:
        Замаскированная строка
    Raises:
        ValueError: Если номер некорректен
    """
    if "счет" in data.lower():
        parts = data.split()
        return f"Счет {get_mask_account(parts[-1])}"
    else:
        parts = data.split()
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


def get_date(date_str: str) -> str:
    """
    Конвертирует дату из формата ISO в "ДД.ММ.ГГГГ".

    Пример:
    >>> get_date("2024-03-11T02:26:18.671407")
    '11.03.2024'
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")