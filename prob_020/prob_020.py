#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def sum_digits(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

print(sum_digits(factorial(100)))
