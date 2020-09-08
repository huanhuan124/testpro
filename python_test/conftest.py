
import pytest

@pytest.fixture()
def login():
    print("这是登录")


#每次自动执行
# @pytest.fixture(autouse=True)
# def open():
#     print("打开浏览器")


@pytest.fixture(scope="module")
def logout():
    print("这是退出")
    yield

    print("这是teardown")
    print("这是最后的操作")
