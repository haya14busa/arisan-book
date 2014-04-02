#include <cstdio>
#include <assert.h>
#include <iostream>

const int MAX_N = 100;

bool could_be_triangle(int a, int b, int c) {
    /*
     * Bool: return if given 3 sticks could be triangle
     */
    int sum = a + b + c;
    int longest = std::max(a, std::max(b, c));
    int lest = sum - longest;
    return longest < lest;
}

int max_circumference(int n, int a[MAX_N]) {
    /*
     * Return max circumference of given sticks
     *  if it cannot make triangle, return 0
     *
     *  O(n^3)
     */
    int max_len = 0;

    // 0 <= i < j < k < n
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (could_be_triangle(a[i], a[j], a[k])) {
                    max_len = std::max(max_len, a[i] + a[j] + a[k]);
                }
            }
        }
    }
    return max_len;
}

int main() {

    // Helper
    assert(could_be_triangle(3, 4, 5) == true);
    assert(could_be_triangle(3, 4, 7) == false);
    assert(could_be_triangle(8, 4, 3) == false);

    int n1 = 5;
    int a1[] = {2, 3, 4, 5, 10};
    int n2 = 4;
    int a2[] = {4, 5, 10, 20};

    assert(max_circumference(n1, a1) == 12);
    assert(max_circumference(n2, a2) == 0);

    puts("All done!");
    return 0;
}
