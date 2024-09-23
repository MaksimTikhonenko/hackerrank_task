import pytest
from The_word_order import word_order


def test_word_order():
    numbers_to_print = ['2', '1', '1']
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]
    assert word_order(words) == (4, '2 1 1')
    # assert word_order("") is None
    # assert word_order(None) is None

