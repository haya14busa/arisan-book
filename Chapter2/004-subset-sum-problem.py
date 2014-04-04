#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 004-subset-sum-problem.py
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

def is_subset_sum(num, integers, given_sum):
    def depth_first_search(i, current_sum):
        ''' Depth First Search O(2^n)
        Recursive call
        i: 0 -> n
        use or not to use `i`th integers
        '''
        if current_sum > given_sum:
            # Optimization
            # Early return if current_sum is over given_sum
            return False

        if i == num: return current_sum == given_sum

        # Do not use `i`th integers
        if depth_first_search(i + 1, current_sum):
            return True

        # Use `i`th integers
        if depth_first_search(i + 1, current_sum + integers[i]):
            return True
        
        # Cannot make subset sum
        return False
    return depth_first_search(0, 0)


def main():
    assert is_subset_sum(4, [1,2,4,7], 13) == True
    assert is_subset_sum(4, [1,2,4,7], 15) == False

    print('All done!')

if __name__ == '__main__':
    main()
