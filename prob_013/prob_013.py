#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def load_numbers(file_name):
    with open(file_name, 'r') as f:
        numbers_raw = f.read()

    numbers = numbers_raw.split('\n')
    numbers.pop()    # Pop the last redundant empty line

    return [int(line) for line in numbers]


if __name__ == '__main__':
    print(str(sum(load_numbers('numbers.txt')))[0:10])
