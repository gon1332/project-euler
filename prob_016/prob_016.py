#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_digits(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res


print(sum_digits(2**1000))
