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


def main():
    assert four_loop(3, 10, [1, 3, 5]) == True
    assert four_loop(3, 9, [1, 3, 5]) == False
    assert four_loop(5, 18, [1, 3, 5, 9, 10]) == True
    print('All done!')

if __name__ == '__main__':
    main()
