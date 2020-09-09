from python import cacl
import pytest
import allure


@allure.feature("测试计算器功能")
class TestCacl:


    def setup(self):
        self.cal = cacl.Cacl()

    @allure.story("测试加法")
    @pytest.mark.parametrize(["a","b","c"],[(1,2,3),(100,200,300),(0,0,0),(-2,-3,-5),(-9,6,-3),(0,-9,-9),(0,4,4)])
    def test_add(self,a,b,c):
        self.cal.add(a,b)
        assert a + b == c


    @allure.story("测试除法的正常情况")
    @pytest.mark.parametrize(["a", "b", "c"],
                             [(1, 2, 0.5), (100, 200, 0.5), (0, 1, 0),(-2, -1, 2.0), (-9, 6, -1.5)])
    def test_div_normal(self,a,b,c):
        self.cal.div(a,b)
        assert a/b == c


    @allure.story("测试除法的异常情况，除数为0，抛出异常")
    @pytest.mark.xfail
    @pytest.mark.parametrize(["a","b"],[(1,0)])
    def test_div_except(self,a,b):
        raise ZeroDivisionError


if __name__ == '__main__':
    TestCacl()
