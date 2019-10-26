#coding=utf-8
'''
This case will be a practice for unitest study:
1. use unittest to set up the precondition and post condition
2. skip one case
3. use unittest assert feature
4. use htmltestrunner to generat report

'''
import unittest
from HtmlTestRunner import HTMLTestRunner
import os
from  testware
 
class myTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #print("=========== Start Now ===========")
        cls.assertTrue(1==1, "========Start Now ========")

    @classmethod
    def tearDownClass(cls):
        #print("=========== All is End ===========")
        cls.assertTrue(2==2, '========= All is End')

    def setUp(self):
        #print("This is precondition!!!")
        self.assertFalse(2>4, "This is precondition!!!")
    
    def tearDown(self):
        #print("This is post condition!!!")
        self.assertTrue(1==1, "This is post condition!!!")

    @unittest.skip("Skip test01")
    def test01(self):
        #print("Test 01: print test 01")
        self.assertTrue(1==2, "Test 01: 1==2?, should fail")

    def test03(self):
        #print("Test 02: print test 02")
        self.assertFalse(1==2,"Test 02: 1 == 2?, shoud pass")

    def test02(self):
        #print("Test 03: print test 03")
        
        self.assertFalse(1==2, "Test 03: 1==2? should fail")

'''
To run the whole test suit, it will run as the order of the test case name asc
'''
if __name__ == "__main__":
    path = os.path.join(os.getcwd()+"\\WebTest\\testResult\\testres01.html")
    res_file = open(path, 'wb')
    unittest.main(testRunner=HTMLTestRunner(report_name="testres01", add_timestamp=False))
    res_file.close()

'''
To run sub of the test suit, it will run according to the order test is added
'''
'''
if __name__ == "__main__":
    subtests = unittest.TestSuite()
    subtests.addTest(myTest('test02'))
    subtests.addTest(myTest('test01'))
   # unittest.TextTestRunner().run(subtests)

    path = os.path.join(os.getcwd()+"\\WebTest\\testResult\\testres01.html")
    res_file = open(path, 'wb')
    #htmlrunner = HtmlTestRunner.HTMLTestRunner(stream=res_file, report_title=u"My first Test Report")
    #htmlrunner.run(subtests)
    runner = HTMLTestRunner(output='test_result')
    runner.run(subtests)
    res_file.close()
'''
