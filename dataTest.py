'''
This is a simple case for Data-Driven Test
'''
import ddt
import unittest
import xlrd
import sys
sys.path.append("C:\\work\\vcPyTest\\WebTest")
from util.excel_util import ExcelUtil

ex = ExcelUtil()
testData = ex.get_data()

@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("===============Start to Run ! =============")

    @classmethod
    def tearDownClass(cls):
        print("=============== End the run ! ==============")

    def setUp(self):
        print("This is the setUp case")

    def tearDown(self):
        print("This is the teardown case")

    @ddt.data(*testData)
   
    def test_add(self, data):
        a,b = data
        a1 = int(a)
        b1 = int(b)
        print("a=",a1, "b=",b1, "a+b=", a1+b1)

if __name__ == "__main__":
    unittest.main()
