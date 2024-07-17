import pytest
from cap import solve


def test_solve():
    assert solve('main') == 'Main'
    assert solve('Main') == 'Main'
    assert solve('') == ''
    assert solve(None) is None
    assert solve('main door') == 'Main Door'
    assert solve('main door bell') == 'Main Door Bell'
    assert solve('m5in 7oor') == 'M5in 7oor'
    assert solve(57) is None
    assert solve('&ain do#r bell') == '&ain Do#r Bell'
    assert solve('main "\n" door bell') == 'Main "\n" Door Bell'
    assert solve(' main door bell ') == ' Main Door Bell '
    assert solve('main  door  bell') == 'Main  Door  Bell'


