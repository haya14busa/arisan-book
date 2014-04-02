#include <cstdio>
#include <assert.h>
#include <algorithm>

const int MAX_N = 50;

bool four_loop(int n, int m, int k[MAX_N]) {
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
    /*
     * O(logn)
     */
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

bool solve_n3logn(int n, int m, int k[MAX_N]) {
    std::sort(k, k + n);

    bool flag = false;

    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            for (int c = 0; c < n; c++) {
                if (binary_search(0, n - 1, k,
                                  m - k[a] - k[b] - k[c])) {
                    flag = true;
                }
            }
        }
    }

    return flag;
}

bool solve_n2logn(int n, int m, int k[MAX_N]) {
    /*
     * O(n^2) & O(n^2logn) -> O(n^2logn)
     */
    int powered_list[MAX_N * MAX_N];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            powered_list[i * n + j] = k[i] + k[j];
        }
    }

    // For binary serach
    std::sort(powered_list, powered_list + n * n);

    for (int a = 0; a < n; a++) {
        for (int b = 0; b < n; b++) {
            if (binary_search(0, n * n -1, powered_list, m - k[a] - k[b])) {
                return true;
            }
        }
    }

    return false;
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
    assert(four_loop(n1, m1, k1) == true);
    assert(four_loop(n2, m2, k2) == false);
    assert(four_loop(n3, m3, k3) == true);

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

    // O(n^3log n)
    assert(solve_n3logn(n1, m1, k1) == true);
    assert(solve_n3logn(n2, m2, k2) == false);
    assert(solve_n3logn(n3, m3, k3) == true);

    // O(n^2log n)
    assert(solve_n2logn(n1, m1, k1) == true);
    assert(solve_n2logn(n2, m2, k2) == false);
    assert(solve_n2logn(n3, m3, k3) == true);

    puts("All done!");
    return 0;
}
