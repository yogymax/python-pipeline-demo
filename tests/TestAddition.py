from database import addition
import unittest
class TestAddition(unittest.TestCase):


    def test_addition_positive(self):
        print('Test Positive Test case')
        result = addition(100,200)
        self.assertEqual(result,300,"Invalid Result for addition 100,200")

    def test_addition_negative(self):
        print('Test Negative Test case')
        try:
            result = addition(100,-200)
        except Exception as e:
            pass
        #self.assertEqual(result,300,"Invalid Result for addition 100,200")

    def test_addition_positive1(self):
        print('test_addition_positive1 ')

    def test_addition_positive2(self):
        print('test_addition_positive2 --')


    def test_addition_positive3(self):
       print('test_addition_positive3 --')
