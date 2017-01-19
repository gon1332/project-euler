#!/usr/bin/env python
# -*- coding: utf-8 -*-

def divisors(num):
    num_divisors = 1
    limit = num
    i = 2
    while i < limit:
        if num % i == 0:
            limit = num // i
            num_divisors += 1
        i += 1

    return num_divisors * 2


idx = 1
triangle_num = 0
while True:
    triangle_num += idx;

    divs = divisors(triangle_num)
    if divs > 500:
        break

    idx += 1

print(idx, ': ', triangle_num, ': ', divs)
