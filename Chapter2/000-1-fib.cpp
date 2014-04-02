#include <cstdio>
#include <assert.h>

int fib(int n) {
    if (n <= 1) return n;
    return fib(n-1) + fib(n-2);
}

int memo[1000000];

int memo_fib(int n) {
    if (n <= 1) return n;
    if (memo[n] != 0) return memo[n];
    return memo[n] = fib(n-1) + fib(n-2);
}

int main() {
    assert(fib(0) == 0);
    assert(fib(1) == 1);
    assert(fib(2) == 1);
    assert(fib(3) == 2);
    assert(fib(10) == 55);

    assert(memo_fib(0) == 0);
    assert(memo_fib(1) == 1);
    assert(memo_fib(2) == 1);
    assert(memo_fib(3) == 2);
    assert(memo_fib(10) == 55);

    puts("All done!");
}
