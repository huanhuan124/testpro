import pytest

class TestData:

    @pytest.mark.parametrize(["a","b"],[(1,2),(4,5)])
    def test_demo(self,a,b):
        print(a+b)