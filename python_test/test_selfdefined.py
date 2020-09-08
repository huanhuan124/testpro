

import  pytest

@pytest.mark.search
def test_search1():
    print("search1")

@pytest.mark.search
def test_search2():
    print("search2")


@pytest.mark.search
def test_search3():
    print("search3")

@pytest.mark.login
def test_login1():
    print("login1")


@pytest.mark.login
def test_login2():
    print("login2")