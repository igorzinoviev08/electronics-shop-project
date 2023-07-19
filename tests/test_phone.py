import pytest


def test_repr_phone(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_phone(phone):
    assert str(phone) == 'iPhone 14'


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 5
    assert phone.number_of_sim == 5
    with pytest.raises(ValueError):
        phone.number_of_sim = 0


def test_add_phone(phone, item_1):
    assert phone + item_1 == 25
    with pytest.raises(TypeError):
        phone + 1
