#include <cstdio>
#include <assert.h>

/* Input: N = 10, M = 12

012345678901

W........WW. 0
.WWW.....WWW 1
....WW...WW. 2
.........WW. 3
.........W.. 4
..W......W.. 5
.W.W.....WW. 6
W.W.W.....W. 7
.W.W......W. 8
..W.......W. 9
*/
int MAX_N = 100;
int MAX_M = 100;

void delete_surrounding_lake(int N, int M, int pos_x, int pos_y, char field[][13]) {
// void delete_surrounding_lake(int N, int M, int pos_x, int pos_y, char **field) {
    /*
     * O(8 * N * M) -> O(N * M)
     * Depth-First Search
     */

    field[pos_x][pos_y] = '.'; // Delete lake at current position

    // Delete surrounding lake
    for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
            int nx = pos_x + dx;
            int ny = pos_y + dy;
            if (0 <= nx && nx < N && 0 <= ny && ny < M && field[nx][ny] == 'W') {
                delete_surrounding_lake(N, M, nx, ny, field);
            }
        }
    }
    return;
}

int lake_counting(int n, int m, char field[][13]) {
// int lake_counting(int n, int m, char **field) {
    /*
     * Lake Counting
     */
    int num_of_lake = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if (field[i][j] == 'W') {
                delete_surrounding_lake(n, m, i, j, field);
                num_of_lake++;
            }
        }
    }
    return num_of_lake;
}

int main(){
    int N1 = 10;
    int M1 = 12;
    char f[11][13]; // field
    // Initialize
    for (int n = 0; n < MAX_N; n++) {
        for (int m = 0; m < MAX_M; m++) {
            f[n][m] = '.';
        }
    }
    f[0][0] = f[0][9] = f[0][10] = \
    f[1][1] = f[1][2] = f[1][3] = f[1][9] = f[1][10] = f[1][11] = \
    f[2][4] = f[2][5] = f[2][9] = f[2][10] = \
    f[3][9] = f[3][10] = \
    f[4][9] = \
    f[5][2] = f[5][9] = \
    f[6][1] = f[6][3] =  f[6][9] = f[6][10] = \
    f[7][0] = f[7][2] =  f[7][4] = f[7][10] = \
    f[8][1] = f[8][3] =  f[8][10] = \
    f[9][2] = f[9][10] = \
         'W';

    assert(lake_counting(10, 12, f) == 3);

    puts("All done!");
    return 0;
}
