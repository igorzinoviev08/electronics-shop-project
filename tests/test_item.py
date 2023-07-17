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


def test_name(item_1):
    item_1.name = 'Смартфон'
    assert item_1.name == 'Смартфон'
    item_1.name = 'СуперСмартфон'
    assert item_1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_item_repr(item_1):
    assert repr(item_1) == "Item('Смартфон', 10000, 20)"


def test_item_str(item_1):
    assert str(item_1) == 'Смартфон'
