from masks import get_mask_card_number, get_mask_account


def main():
    """Пример использования функций маскировки"""
    card_number = input("Введите номер карты (16 цифр): ")
    account_number = input("Введите номер счета: ")

    try:
        print(f"Маска карты: {get_mask_card_number(card_number)}")
        print(f"Маска счета: {get_mask_account(account_number)}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()