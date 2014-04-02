#include <cstdio>
#include <assert.h>
#include <iostream>

int min_time(int L, int n, int x[]) {
    /*
     * L: length
     * n: the number of ants
     * x[i]: the distance from left side of `i`th ants
     *
     * O(n)
     */
    int res = 0;
    for (int i = 0; i < n; i++) {
        res = std::max(res, std::min(x[i], L - x[i]));
    }
    return res;
}

int max_time(int L, int n, int x[]) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        res = std::max(res, std::max(x[i], L - x[i]));
    }
    return res;
}

int main() {
    int L1 = 10;
    int n1 = 3;
    int x1[] = {2, 6, 7};

    assert(min_time(L1, n1, x1) == 4);
    assert(max_time(L1, n1, x1) == 8);

    puts("All done!");
}
