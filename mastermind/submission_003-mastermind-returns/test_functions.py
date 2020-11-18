import unittest
from unittest.mock import patch
from mastermind import *
from io import StringIO
import sys

class MyTestCase(unittest.TestCase):
    '''
    Test Function:

        Tests:

        * a list
        * list length is 4
        * all digits in the list are between 0 and 9(1 to 8) only
    '''

    def test_create_code(self):

        for test in range(100):
            code = create_code()
            self.assertIsInstance(code, list)
            self.assertEqual(4, len(code))
            self.assertNotIn(0,code)
            self.assertNotIn(9, code)

            code = [str(i) for i in code]
            code = ''.join(code)
            is_int = code.isdigit()

            self.assertTrue(is_int)

            
    def test_check_correctness(self):
        '''
        Test function description:

            Tests:
                * a bool value
                * output according to bool value
        '''

        text_trap = StringIO() #Traps the following output in text_trap and doesnt display it
        sys.stdout = text_trap

        self.assertEqual(True, check_correctness(1, 4))
        self.assertEqual('Congratulations! You are a codebreaker!\n',text_trap.getvalue())

        text_trap = StringIO()
        sys.stdout = text_trap

        self.assertEqual(False, check_correctness(3, 3))
        self.assertEqual('Turns left: 9\n',text_trap.getvalue())

        sys.stdout = sys.__stdout__

    @patch("sys.stdin", StringIO('wert\n12345\n1234'))
    def test_get_input(self):

        text_trap = StringIO()
        sys.stdout = text_trap
        
        self.assertEqual(get_answer_input(),"1234")
        self.assertEqual('Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: ',text_trap.getvalue())

        sys.stdout = sys.__stdout__


    @patch("sys.stdin", StringIO('1234\n4312\n'))
    def test_take_turn(self):
        '''
        Test function description:

            Tests:
                * Whether return value is a tuple
                * output  when input is 1234 and 4312

        '''

        text_trap = StringIO()
        sys.stdout = text_trap

        code = [1,2,3,4]
        is_tuple = take_turn(code)

        self.assertIsInstance(is_tuple, tuple)
        self.assertEqual('Input 4 digit code: Number of correct digits in correct place:     4\nNumber of correct digits not in correct place: 0\n',text_trap.getvalue())

        text_trap = StringIO()
        sys.stdout = text_trap
        take_turn(code)
        self.assertEqual('Input 4 digit code: Number of correct digits in correct place:     0\nNumber of correct digits not in correct place: 4\n',text_trap.getvalue())


if __name__ == '__main__':
    unittest.main()



            

