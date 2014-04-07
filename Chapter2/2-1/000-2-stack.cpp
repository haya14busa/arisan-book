#include <stack>
#include <cstdio>
#include <assert.h>

using namespace std;

int main() {
    stack<int> s;
    s.push(1);               // {} -> {1}
    s.push(2);               // {1} -> {1,2}
    s.push(3);               // {1,2} -> {1,2,3}
    printf("%d\n", s.top()); // 3
    s.pop();                 // {1,2,3} -> {1,2}
    printf("%d\n", s.top()); // 2
    s.pop();                 // {1,2} -> {1}
    printf("%d\n", s.top()); // 1
    s.pop();
    return 0;
}
