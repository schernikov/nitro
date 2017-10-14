#!/usr/bin/env python

'''
Created on Oct 13, 2017

@author: schernikov
'''

import argparse, sys

def main():
    parser = arg_parser()
    args = parser.parse_args()
    
    try:
        position = process(args)
    except Exception, e:
        print str(e)
        return -1
    
    print '%d'%(position)
    return 0


def arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('n', help='number of players', type=int)
    parser.add_argument('k', help='count out every k player', type=int)
    parser.add_argument('-x', help='starting position for counting: 1 <= x <= n (default:%(default)d)', required=False, type=int, default=1)
    
    return parser


def process(args):    
    # at this point n, k and x are integers
    if args.n <= 0:
        raise Exception( u"Number of players must be positive. Got %d"%(args.n))
    
    if args.k <= 0:
        raise Exception( u"Count must be positive. Got %d"%(args.k))

    if args.x < 1 or args.x > args.n:
        raise Exception( u"Starting position is not valid. It should be positive and no more than n. Got %d"%(args.x))
    
    index = find_position(args.n, args.k)

    # prepare position shifting to account for starting index
    x = args.x - 1  # zero based start index
    return ((index+x) % args.n) + 1  # return one-based position


def find_position(n, k):
    """
       return zero-based last-standing position index
       https://en.wikipedia.org/wiki/Josephus_problem
    """
    # check degraded and simple cases
    if n == 1:
        return 0 # the only one present

    if k == 1:
        return n-1 # last one
    
    if k == 2:
        # one-step solution O(1)
        L = n - highest_bit(n)
        return 2*L # zero based position index
    
    return find_generic(n, k) if n < k else find_higher(n, k)
    
    
def find_generic(n, k):
    """generic approach; complexity O(n)
    
       Solution:
           if n == 1: return 0
           return (find_lower(n-1, k)+k) % n

       would be quite simple but we need to prepare for huge n values and prevent stack overflows in that case
    """
    g = 0
    for s in xrange(1,n+1):
        g = (g + k) % s

    return g

    
def find_higher(n, k):
    """k <= n, complexity O(k log n)"""
    np = n - n/k
    if np < k:
        g = find_generic(np, k)
    else:
        try:
            g = find_higher(np, k)
        except RuntimeError:
            # capture out-of-stack exception
            g = find_generic(np, k)

    return k*((g - (n % k)) % np)/(k-1)
    

def highest_bit(n):
    count = 0
    while n > 0:
        count += 1
        n >>= 1
        
    return 2**(count-1) # count can not be zero here since n is strictly positive 



if __name__ == '__main__':
    main()
