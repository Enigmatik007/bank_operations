def _validate_number(number: str, required_length: int, name: str) -> None:
    """
    Валидирует номер (карты или счета) по длине и цифровому составу.

    Args:
        number (str): Номер для проверки.
        required_length (int): Минимальная требуемая длина номера.
        name (str): Тип номера ('карты' или 'счета') для сообщения об ошибке.

    Raises:
        ValueError: Если номер короче required_length или содержит нецифровые символы.

    Пример:
        >>> _validate_number("1234", 4, "карты")  # Не вызовет ошибок
        >>> _validate_number("123", 4, "счета")   # Вызовет ValueError
    """
    if len(number) < required_length or not number.isdigit():
        raise ValueError(f"Номер {name} должен содержать минимум {required_length} цифр")


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number (str): 16-значный номер карты без пробелов.

    Returns:
        str: Замаскированный номер в формате 'XXXX XX** **** XXXX'.

    Raises:
        ValueError: Если номер не содержит 16 цифр.

    Пример:
        >>> get_mask_card_number("7000792289606361")
        '7000 79** **** 6361'
    """
    _validate_number(card_number, 16, "карты")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number (str): Номер счета (минимум 4 цифры).

    Returns:
        str: Замаскированный номер в формате '**XXXX'.

    Raises:
        ValueError: Если номер содержит меньше 4 цифр.

    Пример:
        >>> get_mask_account("73654108430135874305")
        '**4305'
    """
    _validate_number(account_number, 4, "счета")
    return f"**{account_number[-4:]}"
