#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 003-ants.py
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


def wrap_ants(L, n, x, func):
    '''Higher Order Function Solving Ants Problem'''
    res = 0
    for i in range(n):
        res = max(res, func(x[i], L - x[i]))
    return res


def min_time(L, n, x):
    # minT = 0
    # for i in range(n):
    #     minT = max(minT, min(x[i], L - x[i]))
    # return minT
    return wrap_ants(L, n, x, min)


def max_time(L, n, x):
    # maxT = 0
    # for i in range(n):
    #     maxT = max(maxT, max(x[i], L - x[i]))
    # return maxT
    return wrap_ants(L, n, x, max)


def main():
    assert min_time(10, 3, [2, 6, 7]) == 4
    assert max_time(10, 3, [2, 6, 7]) == 8
    print('All done!')

if __name__ == '__main__':
    main()
