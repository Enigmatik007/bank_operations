def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX.

    Args:
        card_number: Номер карты (16 цифр без пробелов)

    Returns:
        Замаскированный номер карты

    Raises:
        ValueError: Если номер карты некорректен
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    Args:
        account_number: Номер счета

    Returns:
        Замаскированный номер счета

    Raises:
        ValueError: Если номер счета некорректен
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
