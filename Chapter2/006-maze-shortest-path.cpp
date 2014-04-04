#include <cstdio>
#include <iostream>
#include <assert.h>
#include <queue>

/*
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
*/

const int INF = 100000000;

int solve_maze_with_shortest_path(int N, int M, char maze[10][10]) {
    /*
     * BFS: Breadth-First Search
     *
     * Queue: FIFO (First In First Out)
     */
    // Prepare pair & queue
    typedef std::pair<int, int> P;
    std::queue<P> que;

    int sx; int sy; // Start
    int gx; int gy; // Goal

    //           R  D   L   U
    int dx[4] = {1, 0, -1,  0};
    int dy[4] = {0, 1,  0, -1};

    int distance[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            distance[i][j] = INF; // Initialize
            if (maze[i][j] == 'S') {
                sx = i; sy = j;
            }
            if (maze[i][j] == 'G') {
                gx = i; gy = j;
            }
        }
    }

    // Start!
    que.push(P(sx, sy));
    distance[sx][sy] = 0;
    while (que.size()) {
        // Get front from que
        P p = que.front(); que.pop();

        // Break loop if `p` is the goal
        if (p.first == gx && p.second == gy) break;

        for (int i = 0; i < 4; i++) {
            // Next position
            int nx = p.first + dx[i];
            int ny = p.second + dy[i];

            if (0 <= nx && nx < N && 0 <= ny && ny < M &&
                maze[nx][ny] != '#' && distance[nx][ny] == INF) {
                que.push(P(nx, ny));
                distance[nx][ny] = distance[p.first][p.second] + 1;
            }
        }
    }
    return distance[gx][gy];
}

int main() {

    // Input
    char maze[10][10] = {
        {'#','S','#','#','#','#','#','#','.','#'},
        {'.','.','.','.','.','.','#','.','.','#'},
        {'.','#','.','#','#','.','#','#','.','#'},
        {'.','#','.','.','.','.','.','.','.','.'},
        {'#','#','.','#','#','.','#','#','#','#'},
        {'.','.','.','.','#','.','.','.','.','#'},
        {'.','#','#','#','#','#','#','#','.','#'},
        {'.','.','.','.','#','.','.','.','.','.'},
        {'.','#','#','#','#','.','#','#','#','.'},
        {'.','.','.','.','#','.','.','.','G','#'}
    };

    assert(solve_maze_with_shortest_path(10, 10, maze) == 22);
    puts("All done!");
}


