import pytest
from The_minion_game import minion_game, calculate_score, build_substring


def test_minion_game():
    assert minion_game('BANANA') == ('Stuart', 12)
    assert minion_game('') == 'Draw'
    assert minion_game('BANAAAA') == ('Kevin', 16)


def test_calculate_score_vowels():
    substrings = ['B', 'BA', 'BAN', 'A', 'AN', 'N']
    sub = ['B', ' ', 'BA', 'BAN', 'A', 'AN', 'N']
    sub_2 = ['B', 'BA', 'A', 'AN', 'N', '&&&']

    filt = lambda x: x[0] in 'AEIOUaeiou'

    assert calculate_score(substrings, filt) == 2
    assert calculate_score(sub, filt) == 2
    assert calculate_score(sub_2, filt) == 2


def test_calculate_score_consonants():
    substrings = ['B', 'BA', 'BAN', 'A ', 'AN', 'N']
    sub = ['B', ' ', 'BA', 'BAN', 'A', 'AN', 'N']
    sub_2 = ['B', 'BA', 'A', 'AN', 'N', '&&&']

    filt = lambda x: x[0] not in 'AEIOUaeiou'

    assert calculate_score(substrings, filt) == 4
    assert calculate_score(sub, filt) == 5
    assert calculate_score(sub_2, filt) == 4


def test_build_substring():
    assert build_substring('BAN') == ['B', 'BA', 'BAN', 'A', 'AN', 'N']
    assert build_substring('BaN') == ['B', 'Ba', 'BaN', 'a', 'aN', 'N']
    assert build_substring('ban') == ['b', 'ba', 'ban', 'a', 'an', 'n']
    assert build_substring('') == []
    assert build_substring('ban BAN') == ['b', 'ba', 'ban', 'ban ', 'ban B',
                                          'ban BA', 'ban BAN', 'a', 'an', 'an ',
                                          'an B', 'an BA', 'an BAN', 'n', 'n ',
                                          'n B', 'n BA', 'n BAN', ' ', ' B', ' BA',
                                          ' BAN', 'B', 'BA', 'BAN', 'A', 'AN', 'N']



