import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize('card_num, expected', [
    ('1234567890123456', '1234 56** **** 3456'),
    ('5555444433332222', '5555 44** **** 2222'),
    ('1111222233334444', '1111 22** **** 4444')
])
def test_get_mask_card_number(card_num, expected):
    assert get_mask_card_number(card_num) == expected

@pytest.mark.parametrize('account_num, expected', [
    ('123456789012', '**9012'),
    ('9876543210987654', '**7654'),
    ('0000000000009999', '**9999')
])
def test_get_mask_account(account_num, expected):
    assert get_mask_account(account_num) == expected
