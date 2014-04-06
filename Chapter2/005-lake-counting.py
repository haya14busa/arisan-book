#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 005-lake-counting.py
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

'''
Input: N = 10, M = 12

012345678901

W........WW.  0
.WWW.....WWW  1
....WW...WW.  2
.........WW.  3
.........W..  4
..W......W..  5
.W.W.....WW.  6
W.W.W.....W.  7
.W.W......W.  8
..W.......W.  9

'''

from copy import deepcopy

def lake_counting(n, m, field):
    def is_in_field(x, y):
        ''' Boolean: position x, y is in the field?  '''
        return 0 <= x < n and 0 <= y < m

    def is_lake(x, y):
        ''' Boolean: the position is lake? '''
        return field[x][y] == 'W'

    def delete_lake(x, y):
        field[x][y] = '.'

    def delete_surrounding_lakes(pos_x, pos_y):
        '''Delete surrouding lakes
        Depth-First Search
        O(N * M)
        '''
        # Delete lake at current position
        delete_lake(pos_x, pos_y)

        # Delete surroinding rakes
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                next_x, next_y = pos_x + dx, pos_y + dy
                if is_in_field(next_x, next_y) and is_lake(next_x, next_y):
                    delete_surrounding_lakes(next_x, next_y)

    num_of_lakes = 0
    # Search all field
    for i in range(n):
        for j in range(m):
            if is_lake(i, j):
                delete_surrounding_lakes(i, j)
                num_of_lakes += 1
    return num_of_lakes


def main():
    # field
    # f = [['.' for i in range(12)] for i in range(10)]
    # f[0][0] = f[0][9] = f[0][10] = \
    # f[1][1] = f[1][2] = f[1][3] = f[1][9] = f[1][10] = f[1][11] = \
    # f[2][4] = f[2][5] = f[2][9] = f[2][10] = \
    # f[3][9] = f[3][10] = \
    # f[4][9] = \
    # f[5][2] = f[5][9] = \
    # f[6][1] = f[6][3] =  f[6][9] = f[6][10] = \
    # f[7][0] = f[7][2] =  f[7][4] = f[7][10] = \
    # f[8][1] = f[8][3] =  f[8][10] = \
    # f[9][2] = f[9][10] = \
    #      'W';

    f = [
    ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
    ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.']
    ]

    f2 = deepcopy(f)
    f2[9][6] = 'W'

    print('Input:')
    for line in f:
        print(''.join(line))

    assert lake_counting(10, 12, f) == 3
    assert lake_counting(10, 12, f2) == 4

    print('All done!')

if __name__ == '__main__':
    main()
