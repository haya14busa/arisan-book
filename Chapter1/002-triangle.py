#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 002-triangle.py
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


def could_be_triangle(a, b, c):
    longest = max(a, b, c)
    sum_of_len = a + b + c
    rest = sum_of_len - longest
    return longest < rest


def max_circumference(n, a):
    """max_circumference
    O(n^3)
    """
    max_length = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if could_be_triangle(a[i], a[j], a[k]):
                    max_length = max(max_length, a[i] + a[j] + a[k])
    return max_length


def main():
    assert could_be_triangle(3, 4, 5) == True
    assert could_be_triangle(3, 4, 7) == False
    assert could_be_triangle(8, 4, 3) == False

    assert max_circumference(5, [2, 3, 4, 5, 10]) == 12
    assert max_circumference(4, [4, 5, 10, 20]) == 0

    print('All done!')

if __name__ == '__main__':
    main()
