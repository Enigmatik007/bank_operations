"""Главный скрипт для работы с банковскими операциями."""

from src.masks import get_mask_card_number  # Убрали неиспользуемый импорт
from src.widget import get_date, mask_account_card


def main() -> None:
    """Точка входа в приложение."""
    print('Демонстрация работы модулей:')
    print('\nМаскирование карт:')
    print(get_mask_card_number('7000792289606361'))
    print('\nФорматирование данных:')
    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(get_date('2024-03-11T02:26:18.671407'))


if __name__ == '__main__':
    main()
