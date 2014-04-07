#include <cstdio>
#include <iostream>
#include <assert.h>

int minimum_coins_to_pay(int n_of_coins[6], int price) {
    const int Values_of_coins[6] = {1, 5, 10, 50, 100, 500};

    int rest_price = price;
    int n_of_payed_coins = 0;

    for (int i = 5; i >= 0; i--) {
        int n_of_i_th_coin = std::min(rest_price / Values_of_coins[i],
                                      n_of_coins[i]);
        rest_price -= n_of_i_th_coin * Values_of_coins[i];
        n_of_payed_coins += n_of_i_th_coin;
    }
    return n_of_payed_coins;
}

int main() {
    int c1[6] = {3, 2, 1, 3, 0, 2};
    int price1 = 620;

    assert(minimum_coins_to_pay(c1, price1) == 6);
    puts("All done!");
    return 0;
}
