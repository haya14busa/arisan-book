#include <cstdio>
#include <assert.h>

bool is_subset_sum(int i, int sum, int n, int a[], int k) {
    /*
     * Depth-First Search
     */
    if (i == n) return sum == k;

    // do not use a_i
    if (is_subset_sum(i + 1, sum, n, a, k)) return true;

    // use a_i
    if (is_subset_sum(i + 1, sum + a[i], n, a, k)) return true;

    return false;
}

int main() {
    /*
     * n   : the number of integers
     * a_i : value of integers
     * k   : expected subset sum
     */
    int n1 = 4;
    int a1[] = {1,2,4,7};
    int k1 = 13;

    int n2 = 4;
    int a2[] = {1,2,4,7};
    int k2 = 15;

    assert(is_subset_sum(0, 0, n1, a1, k1) == true);
    assert(is_subset_sum(0, 0, n2, a2, k2) == false);

    puts("All done!");
    return 0;
}
