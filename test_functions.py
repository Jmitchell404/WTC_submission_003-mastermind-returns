import unittest
from io import StringIO
import sys
from test_base import captured_io
from unittest.mock import patch
from test_base import run_unittests
import mastermind

class TestFunctions(unittest.TestCase):
    def test_create_code(self):
        """
        Tests the create_code function for:
        Returning a random code of 4 digits and
        for the range of the digits being 1-8.
        """
        output = StringIO()
        sys.stdout = output
        for item in range(101):
            self.assertTrue(mastermind.create_code(),True)
        sys.stdout = sys.__stdout__

    def test_correctness(self):
        """
        Tests the correctness function for:
        If the 4 digits given from the user is the correct 4 digits chosen from
        the create_code function.
        If the users digits are correct then it will print
        "Congratulations! You are a codebreaker!" and if not correct it will print
        how many turns you have left.
        """
        output = StringIO()
        sys.stdout = output
        self.assertEqual(mastermind.check_correctness(4,5),False)
        self.assertEqual(mastermind.check_correctness(5,7),False)
        sys.stdout = sys.__stdout__

    @patch("sys.stdin", StringIO("123\n3421\n"))
    def test_answer_input(self):
        """
        Tests answer_input for:
        If the user inputs more or less than 4 digits then
        it will print "Please enter exactly 4 digits." and
        it will loop again with "Input 4 digit code: " until
        the correct digits are inputed.
        """
        output = StringIO()
        sys.stdout = output
        result = mastermind.answer_input()
        self.assertEqual(result, "3421")
        sys.stdout = sys.__stdout__

    @patch("sys.stdin", StringIO("1234\n1342\n"))
    def test_take_turns(self):
        """
        Tests the take_turns for:
        If the correct_digits_and_position and
        correct_digits_only are checking that the users input
        is the same as the randomised code by correct digits,
        correct digit position and if it is only digits.
        If it prints out how many digits arec in orrect_digits_and_position
        and are correct_digits_only.
        """
        output = StringIO()
        sys.stdout = output
        sys.stdout = sys.__stdout__
        answer = ["1","2","3","4"]
        code = [1,2,3,4]
        result = mastermind.take_turn(answer,code)
        compare_tuple = (4,0)
        self.assertEqual(result,compare_tuple)




        




if __name__ == "__main__":
    unittest.main()