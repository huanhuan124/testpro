import pytest




@pytest.mark.parametrize("test_input,expected",[("3+5",8),("7-6",2)])
# @pytest.fixture(params=[2,3])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[3,4])
def test_foo(x,y):
    print(f"测试组合数据x:{x},y:{y}")
    raise NameError


#方法名作为参数

test_usr_data = ['Tom','Jerry']
@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 准备打开首页登录，登录用户{user}")
    return user


@pytest.mark.skip("跳过这条用例")
#indirect=True , 可以把传过来的参数当函数来执行，如果不加的话，不会执行login_r中的内容
@pytest.mark.parametrize("login_r",test_usr_data,indirect=True )
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ''






















