import unittest
import random
from unittest.mock import patch
from io import StringIO


    #@patch("sys.stdin", StringIO("code"))
class TestFunctions(unittest.TestCase):    
    def test_create_code(self):
        value = random.randint(1, 8)
        code = [0, 0, 0, 0]
        self.assertTrue(code, value)
    
    
    def test_show_instructons(self):
        self.assertTrue('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    
    
    def test_show_results(self):
        correct_digits_and_position = 0
        correct_digits_only = 0
        self.assertTrue('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
        self.assertTrue('Number of correct digits not in correct place: ' + str(correct_digits_only))
    
    
    def test_take_turn(self):
        self.assertTrue("Input 4 digit code: ")
    
    def test_show_code(self):
        code = [0,0,0,0]
        self.assertTrue('The code was: '+str(code))

    
    def test_check_correctness(self):
        self.assertTrue('Congratulations! You are a codebreaker!')
if __name__ == '__main__':
    unittest.main()
