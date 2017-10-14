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


    def try_values(self, n, k, shift=None):
        args = ['%d'%(n), '%d'%(k)]
        if shift is not None:
            args.insert(0, '-x')
            args.insert(1, '%d'%(shift))

        return counting.process(self.parser.parse_args(args))
    
    
    def try_range(self, rr, k):
        for idx in xrange(len(rr)):
            self.assertEqual(self.try_values(idx+1, k), rr[idx])


    def test_invalid(self):
        with self.assertRaises(SystemExit) as cm:
            with test.helper.OutputSuppressor(): # ignore annoying stderr complains
                counting.process(self.parser.parse_args([]))
            
        self.assertEqual(cm.exception.code, 2)

        with self.assertRaises(SystemExit) as cm:
            with test.helper.OutputSuppressor(): # ignore annoying stderr complains
                counting.process(self.parser.parse_args(['a', 'b']))
                
        self.assertEqual(cm.exception.code, 2)
        
        with self.assertRaises(Exception):
            with test.helper.OutputSuppressor(): # ignore annoying stderr complains
                counting.process(self.parser.parse_args(['-x', '5', '1', '1']))
                
        self.assertEqual(cm.exception.code, 2)


    def test_negatives(self):
        with self.assertRaises(Exception):
            self.try_values(-1, -1)
            
        with self.assertRaises(Exception):
            self.try_values(-1, 1)
            
        with self.assertRaises(Exception):
            self.try_values(1, -1)
            
            
    def test_ones(self):
        k=1
        rr = range(1, 10)
        self.try_range(rr, k)
        
        
    def test_twos(self):
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12, 13, 14, 15, 16]
        rr = [1, 1, 3, 1, 3, 5, 7, 1, 3, 5, 7, 9, 11, 13, 15, 1]
        k = 2
        self.try_range(rr, k)


    def test_threes(self):
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        rr = [1, 2, 2, 1, 4, 1, 4, 7, 1, 4]
        k = 3
        self.try_range(rr, k)
        
        
    def test_fours(self):
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        rr = [1, 1, 2, 2, 1, 5, 2, 6, 1, 5]
        k = 4
        self.try_range(rr, k)
        
        
    def test_shifted(self):
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        rr = [1, 1, 2, 2, 1, 5, 2, 6, 1, 5]
        k = 4
        def shifted_result(n, shift):
            r = rr[n-1] - 1 # zero based position
            sh = shift - 1  # zero based position
            return ((r+sh)%n)+1 # one based position

        for n in xrange(1, len(rr)+1):
            for shift in xrange(1, n+1):
                self.assertEqual(self.try_values(n, k, shift=shift), shifted_result(n, shift))
        
        
    def test_huge(self):
        self.assertEqual(self.try_values(10000000, 100), 2444746)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCounting']
    unittest.main()
