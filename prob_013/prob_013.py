#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def load_numbers(file_name):
    with open(file_name, 'r') as f:
        numbers_raw = f.read()

    numbers = numbers_raw.split('\n')
    numbers.pop()    # Pop the last redundant empty line

    return [list(map(int, line)) for line in numbers]


if __name__ == '__main__':
    numbers = load_numbers('numbers.txt')

    res = [0]*51

    # Find intermediate sums
    for col in range(50):
        for number in range(100):
            res[col] += numbers[number][col]

    # Move the carries
    for i in range(50, 0, -1):
        d = res[i] // 10
        res[i] -= d * 10
        res[i-1] += d

    # Move the carries for the front digits
    while res[0] >= 10:
        d = res[0] // 10
        res[0] -= d * 10
        res.insert(0, d)

    print(''.join(map(str, res[0:10])))
