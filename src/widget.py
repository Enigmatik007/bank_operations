"""Модуль виджетов для форматирования банковских данных."""

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Автоматически определяет тип (карта/счет) и применяет соответствующую маскировку.

    Args:
        data (str): Строка формата "Тип Номер" (например, "Visa 7000792289606361").

    Returns:
        str: Замаскированная строка.

    Raises:
        ValueError: Если номер не проходит валидацию.

    Примеры:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'
        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    if "счет" in data.lower():
        parts = data.split()
        return f"Счет {get_mask_account(parts[-1])}"
    else:
        parts = data.split()
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


def get_date(date_str: str) -> str:
    """
    Конвертирует дату из ISO-формата в русский формат.

    Args:
        date_str (str): Дата в формате ISO (например, "2024-03-11T02:26:18.671407").

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ".

    Пример:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")
