#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 007-coin.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#=============================================================================

def min_coins_of_given_price(num_of_each_coins, price):
    """min_coins_of_given_price

    Return the number of minimum coins with given price

    :param num_of_each_coins: the number of each coins
        [C1, C5, C10, C50, C100, C500]

    :param price:
        Given price to py
    """
    VALUES_OF_COINS = [1, 5, 10, 50, 100, 500]
    n_of_payed_coins = 0 # Answer
    rest_price = price # Rest price to pay

    # To pay with bigger coins as much as possible
    num_of_each_coins.reverse()

    for i_th, num_of_coin in enumerate(num_of_each_coins):
        n_of_payed_i_th_coin = min(
            int(rest_price / VALUES_OF_COINS[5 - i_th]),
            num_of_coin)
        n_of_payed_coins += n_of_payed_i_th_coin
        rest_price -= n_of_payed_i_th_coin * VALUES_OF_COINS[5 - i_th]
    return n_of_payed_coins



def main():
    assert(min_coins_of_given_price([3, 2, 1, 3, 0, 2], 620) == 6);
    print('All done!')

if __name__ == '__main__':
    main()
