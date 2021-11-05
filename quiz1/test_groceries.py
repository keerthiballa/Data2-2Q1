from quiz1.groceries import checkout
import unittest
import unittest.mock
from io import StringIO
#from quiz1.groceries import checkout


class GroceriesTest(unittest.TestCase):

 
    def test_groc1(self):
        expected = 54.69
        
        groc_dict = {
            'oatmeal': 4.59,
            'beefroast': 12.56,
            'cottagecheese': 3.99,
            'yogurt': 3.19,
            'nuts': 15.99,
            'bread': 4.99,
        }
        actual = checkout(100.0, groc_dict)
        self.assertEqual(expected, actual, 4)

    def test_groc2(self):
        expected = 4.5
        
        groc_dict = {
            'cereal': 3.69,
            'milk': 2.99,
            'carrots': 2.19,
            'potatoes': 3.99,
            'besam': 4.66,
            'paneer': 6.99,
            'cumin seeds': 0.99,
        }
        actual = checkout(30.0, groc_dict)
        self.assertAlmostEqual(expected, actual, 4)
      

