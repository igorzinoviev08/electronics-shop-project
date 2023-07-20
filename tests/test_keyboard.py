import pytest


def test_language(keyboard):
    assert str(keyboard) == "Dark Project KD87A"
    assert str(keyboard.language) == "EN"
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
