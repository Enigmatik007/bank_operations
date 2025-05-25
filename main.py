from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


def main():
    """Проверка всех функций"""
    # Проверка масок (старые функции)
    card = input("Введите номер карты (16 цифр): ")
    account = input("Введите номер счета: ")

    try:
        print(f"\nМаска карты: {get_mask_card_number(card)}")
        print(f"Маска счета: {get_mask_account(account)}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Проверка новых функций
    data = input("\nВведите 'Тип Номер' (напр. 'Visa 1234...' или 'Счет 1234...'): ")
    print(f"Результат mask_account_card: {mask_account_card(data)}")

    date = input("Введите дату (ГГГГ-ММ-ДДTHH:MM:SS): ")
    print(f"Результат get_date: {get_date(date)}")


if __name__ == "__main__":
    main()
