"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(item_1, item_2):
    assert item_1.calculate_total_price() == 200000.0
    assert item_2.calculate_total_price() == 100000.0


def test_apply_discount(item_1, item_2):
    Item.pay_rate = 0.8
    item_1.apply_discount()
    item_2.apply_discount()
    assert item_1.price == 8000.0
    assert item_2.price == 16000.0
