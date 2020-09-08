


import pytest

# @pytest.fixture()
# def login():
#     print("这是登录")

def test_one(login):
    print("test1，需要先登录")

def test_two(login):
    print("test2，需要先登录")

def test_three():
    print("test3，不需要先登录")


def test_four(logout):
    print("test4")

def test_five(logout):
    print("test5")




if __name__ == '__main__':
    pytest.main()