'''
Created on Oct 13, 2017

@author: schernikov
'''
import unittest

import test.helper
import counting

class TestCounting(unittest.TestCase):


    def setUp(self):
        self.parser = counting.arg_parser()


    def tearDown(self):
        pass


    def try_values(self, n, k):
        return counting.process(self.parser.parse_args(['%d'%(n), '%d'%(k)]))
    
    
    def try_range(self, nn, k):
        for idx in xrange(len(nn)):
            self.assertEqual(self.try_values(idx+1, k), nn[idx])


    def test_invalid(self):
        with self.assertRaises(SystemExit) as cm:
            with test.helper.OutputSuppressor(): # ignore annoying stderr complains
                counting.process(self.parser.parse_args([]))
            
        self.assertEqual(cm.exception.code, 2)

        with self.assertRaises(SystemExit) as cm:
            with test.helper.OutputSuppressor(): # ignore annoying stderr complains
                counting.process(self.parser.parse_args(['a', 'b']))
            
        self.assertEqual(cm.exception.code, 2)

    def test_negatives(self):
        with self.assertRaises(Exception):
            self.try_values(-1, -1)
            
        with self.assertRaises(Exception):
            self.try_values(-1, 1)
            
        with self.assertRaises(Exception):
            self.try_values(1, -1)
            
            
    def test_ones(self):
        self.try_range(range(1, 10), 1)
        
        
    def test_twos(self):
        results = [1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1]
        self.try_range(results, 2)


    def test_threes(self):
        results = [1, 2, 2, 1, 4, 1, 4, 7, 1, 4]
        self.try_range(results, 3)
        
        
    def test_fours(self):
        results = [1, 1, 2, 2, 1, 5, 2, 6, 1, 5]
        self.try_range(results, 4)
        
        
    def test_huge(self):
        self.assertEqual(self.try_values(10000000, 100), 2444746)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCounting']
    unittest.main()
