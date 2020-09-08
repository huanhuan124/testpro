import pytest

def test_a():
    print("aaaaa")
    assert 'a' in 'abc'

def test_b():
    print("bbbbb")
    assert '1' not in '123'

def test_c():
    print("ccccc")
    assert 1 == 1