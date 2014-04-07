// XXX: These codes are just a example.


int MAX_N = 10000;

bool used[MAX_N];
int perm[MAX_N];

// {0,1,2,3,4,.., n-1}の並び替え、n!通りの生成

void permutation1(int pos, int n) {
    if (pos == n) {
        /*
         * Operate something to perm
         */
        return ;
    }

    for (int i = 0; i < n; i++) {
        if (!used[i]) {
            perm[pos] = i;
            // turn on i used flag
            used[i] = true;
            permutation1(pos + 1, n);
            // turn off back i used flag
            used[i] = false;
        }
    }
    return ;
}

#include <algorithm>

int perm2[MAX_N];

void permutation2(int n) {
    for (int i = 0; i < n; i++) {
        perm2[i] = i;
    }
    do {
        /*
         * Operate something to perm
         */
    } while (next_permutation(perm2, perm2 + n));
    return ;
}
