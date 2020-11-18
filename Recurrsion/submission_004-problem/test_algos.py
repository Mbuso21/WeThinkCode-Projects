import unittest
import super_algos

class MyTestCases(unittest.TestCase):

    def test_find_min(self):
        '''
        Test Function:

            * Tests if all instructions are followed for find_min(list)
        '''
        self.assertEqual(super_algos.find_min(''),-1)
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.find_min([1,'a',5,6]), -1)
        self.assertEqual(super_algos.find_min([1,1.3,5,6]), -1)
        self.assertEqual(super_algos.find_min([1,2,3,4]),min([1,2,3,4]))

    def test_sum_all(self):
        '''
        Test Function:

            * Tests if all instructions are followed for sum_all(list)
        '''
        self.assertEqual(super_algos.sum_all(''), -1)
        self.assertEqual(super_algos.sum_all([]), -1)
        self.assertEqual(super_algos.sum_all([1,'a',3,4]), -1)
        self.assertEqual(super_algos.find_min([1,1.3,5,6]), -1)
        self.assertEqual(super_algos.sum_all([1,2,3,4]),sum([1,2,3,4]))

    def test_possible_string(self):
        '''
        Test Function:

            * Tests if all instructions are followed for find_possible_srings(list, int)
        '''

        self.assertIsInstance(super_algos.find_possible_strings(['a', 'b'], 2),list)
        self.assertEqual([],super_algos.find_possible_strings(['1','a'], 1))
        self.assertEqual([],super_algos.find_possible_strings([1,2,3,4],2))
        self.assertEqual([], super_algos.find_possible_strings(['','a'], 2))
        self.assertEqual(['a','a','a'],super_algos.find_possible_strings(['a'],3))
        self.assertEqual(['aa', 'ab', 'ba', 'bb'], super_algos.find_possible_strings(['a','b'], 2))




if __name__ == '__main__':
    unittest.main()
        