#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 001-lottery.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#=============================================================================

MAX_N = 50


def four_loop(n, m, k):
    """O(n^4)"""
    # n: the number of lots
    # m: the expected sum
    # k: choosed_list contains 4 numbers
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if k[a] + k[b] + k[c] + k[d] == m:
                        return True
    return False

def binary_search(sorted_list, query):
    """O(logn)"""
    def binary_helper(begin, end):
        if begin == end and not sorted_list[begin] == query:
            return False
        middle = int((begin + end) / 2)
        if sorted_list[middle] == query:
            return True
        elif sorted_list[middle] < query:
            return binary_helper(middle + 1, end)
        else:
            return binary_helper(begin, middle)
    return binary_helper(0, len(sorted_list) - 1)


def improved_lottery(n, m, k):
    """O(n^2logn)"""
    powered_list = [k[i] + k[j] for i in range(n) for j in range(n)]
    # Sort for binary search
    powered_list.sort()
    for i in range(n):
        for j in range(n):
            if binary_search(powered_list, m - k[i] - k[j]):
                return True
    return False


def main():
    assert four_loop(3, 10, [1, 3, 5]) == True
    assert four_loop(3, 9, [1, 3, 5]) == False
    assert four_loop(5, 18, [1, 3, 5, 9, 10]) == True


    # binary search
    assert binary_search([1,3,5,6,7,10], 1) == True
    assert binary_search([1,3,5,6,7,10], 5) == True
    assert binary_search([1,3,5,6,7,10], 10) == True
    assert binary_search([1,3,5,6,7,10], 11) == False
    assert binary_search([1,3,5,6,7,10], 2) == False
    assert binary_search([1,3,5,6,7,10], -10000) == False

    assert binary_search([1,3,5,6,7], 1) == True
    assert binary_search([1,3,5,6,7], 3) == True
    assert binary_search([1,3,5,6,7], 5) == True
    assert binary_search([1,3,5,6,7], 6) == True
    assert binary_search([1,3,5,6,7], 7) == True
    assert binary_search([1,3,5,6,7], 8) == False

    # Improve
    assert improved_lottery(3, 10, [1, 3, 5]) == True
    assert improved_lottery(3, 9, [1, 3, 5]) == False
    assert improved_lottery(5, 18, [1, 3, 5, 9, 10]) == True
    assert improved_lottery(5, 18, [10, 3, 5, 9, 1]) == True
    assert improved_lottery(5, 18, [10, 11, 9, 300, 1]) == False

    print('All done!')

if __name__ == '__main__':
    main()
