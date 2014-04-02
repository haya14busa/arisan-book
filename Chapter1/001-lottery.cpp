#include <cstdio>
#include <assert.h>
#include <algorithm>
#include <deque>
#include <iostream>
#include <list>

const int MAX_N = 50;

int four_loop(int n, int m, int k[MAX_N]) {
    /*
     * O(n^4)
     */

    // Prepare flag:
    //  found the combintation of 4 cards, sum of them equals to m?
    bool flag = false;

    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            for (int c = 0; c < n; c++) {
                for (int d = 0; d < n; d++) {
                    if (k[a] + k[b] + k[c] + k[d] == m) {
                        flag = true;
                    }
                }
            }
        }
    }

    return flag;
}

bool binary_search(int begin, int end, int array[], int x) {
    // The number of element is 1 && equals to x
    if (begin == end && array[begin] != x) return false;

    // binary_search
    int i = (begin + end) / 2;
    if (array[i] == x) {
        return true;
    } else if (array[i] < x) {
        // recursive call
        return binary_search(i+1, end, array, x);
    } else {
        return binary_search(begin, i, array, x);
    }
}

int main() {
    // n: the number of lot
    // m: the sum of 4 cards
    // int n, m, k[MAX_N];

    int n1 = 3;
    int m1 = 10;
    int k1[] = {1, 3, 5};

    int n2 = 3;
    int m2 = 9;
    int k2[] = {1, 3, 5};

    int n3 = 5;
    int m3 = 18;
    int k3[] = {1, 3, 5, 9, 10}; // -> {1, 3, 5, 9}

    // 4 Loop
    assert(four_loop(n1, m1, k1) == 1);
    assert(four_loop(n2, m2, k2) == 0);
    assert(four_loop(n3, m3, k3) == 1);

    // Binary-search
    assert(binary_search(0, 2, k1, -1) == false);
    assert(binary_search(0, 2, k1, 1) == true);
    assert(binary_search(0, 2, k1, 3) == true);
    assert(binary_search(0, 2, k1, 5) == true);
    assert(binary_search(0, 2, k1, 9) == false);
    assert(binary_search(0, 2, k1, 300) == false);
    int list[4] = {1,2,3,4};
    assert(binary_search(0, 3, list, 1) == true);
    assert(binary_search(0, 3, list, 2) == true);
    assert(binary_search(0, 3, list, 3) == true);
    assert(binary_search(0, 3, list, 4) == true);
    assert(binary_search(0, 3, list, 5) == false);
    assert(binary_search(0, 3, list, 50000) == false);

    puts("All done!");
    return 0;
}
