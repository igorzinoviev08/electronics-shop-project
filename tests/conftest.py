import pytest
from src.item import Item
from src.phone import Phone
@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def item_1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def item_2():
    return Item("Ноутбук", 20000, 5)


