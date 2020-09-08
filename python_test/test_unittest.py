

import unittest

class demo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("demo1 setupclass \n")

    def setUp(self):
        print("demo1 setup")


    def test_case1(self):
        print("demo1 testcase1")


    def test_case2(self):
        print("demo1 testcase2")

    def test_case3(self):
        print("demo1 testcase3")




    def tearDown(self):
        print("demo1 teardown")

    @classmethod
    def tearDownClass(cls):
        print("demo1 teardownclass \n")


class demo2(unittest.TestCase):


    def test_case1(self):
        print("demo2 testcase1")

    def test_case2(self):
        print("demo2 testcase2")



class demo3(unittest.TestCase):


    def test_case1(self):
        print("demo3 testcase1")

    def test_case2(self):
        print("demo3 testcase2")


if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(demo1("test_case1"))
    # suite.addTest(demo2("test_case2"))
    # unittest.TextTestRunner().run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo2)
    # suiteall = unittest.TestSuite([suite1, suite2])
    # unittest.TextTestRunner().run(suiteall)

    discover = unittest.defaultTestLoader.discover("./",pattern="test*.py")
    unittest.TextTestRunner().run(discover)
















