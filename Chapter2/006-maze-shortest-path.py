#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 006-maze-shortest-path.py
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

from queue import Queue
from copy import deepcopy

'''Input: N=10, M=10

#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
'''


def shortest_path_of_maze(N, M, sx, sy, gx, gy, maze):
    INF = 10000000 # Infinity
    def is_goal(x, y):
        return x == gx and y == gy

    def is_wall(x, y):
        return maze[x][y] == '#'

    def is_in_maze(x, y):
        return 0 <= x < N and 0 <= y < M

    def is_searched(x, y):
        return distance[x][y] != INF

    distance = [[ INF for i in range(N)] for i in range(M)]
    que = Queue()

    que.put((sx, sy))
    distance[sx][sy] = 0

    #     L D R U
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while not que.empty():
        p = que.get()
        if is_goal(p[0], p[1]): break
        for i in range(4):
            nx = p[0] + dx[i]; ny = p[1] + dy[i]
            if is_in_maze(nx, ny) and not is_wall(nx, ny) and not is_searched(nx, ny):
                que.put((nx, ny))
                distance[nx][ny] = distance[p[0]][p[1]] + 1
    return distance[gx][gy]


def main():
    maze = [
        ['#','S','#','#','#','#','#','#','.','#'],
        ['.','.','.','.','.','.','#','.','.','#'],
        ['.','#','.','#','#','.','#','#','.','#'],
        ['.','#','.','.','.','.','.','.','.','.'],
        ['#','#','.','#','#','.','#','#','#','#'],
        ['.','.','.','.','#','.','.','.','.','#'],
        ['.','#','#','#','#','#','#','#','.','#'],
        ['.','.','.','.','#','.','.','.','.','.'],
        ['.','#','#','#','#','.','#','#','#','.'],
        ['.','.','.','.','#','.','.','.','G','#'],
    ]
    #                             N,  M,sx,sy,gx,gy, Maze
    assert shortest_path_of_maze(10, 10, 0, 1, 9, 8, maze) == 22
    maze2 = deepcopy(maze)
    maze2[8][8] = '.'
    assert shortest_path_of_maze(10, 10, 0, 1, 9, 8, maze2) == 16

    print('All done!')

if __name__ == '__main__':
    main()

