#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc_chain_len(num):
    chain_len = 1
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1

        if num in chains_dict:
            chain_len += chains_dict[num]
            break

        if num == 1:
            break

        chain_len += 1

    return chain_len


if __name__ == '__main__':
    biggest_chain_num = 0
    biggest_chain_len = 0

    chains_dict = {}

    for starting_num in range(1, 1000000):

        chain_len = calc_chain_len(starting_num)

        if chain_len > biggest_chain_len:
            biggest_chain_len = chain_len
            biggest_chain_num = starting_num

        chains_dict[starting_num] = chain_len

    print(biggest_chain_num, ':', biggest_chain_len)
