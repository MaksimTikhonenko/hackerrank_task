import pytest
from The_minion_game import minion_game, count_words


def test_minion_game():
    assert minion_game('BANANA') == ('Stuart', 12)
    assert minion_game(' ') == 'Draw'
    assert minion_game('BANAAAA') == ('Kevin', 16)


def test_count_words():
    assert count_words('BANANA') == (12, 9)
    assert count_words('BaN') == (6, 0)
    assert count_words('ban') == (6, 0)
    assert count_words('') == (0, 0)
    assert count_words('ban BAN') == (26, 2)
