#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    return pow(2 << n, n + 1, (4 << 2*n) - (2 << n) - 1) % (2 << n)

n = 2
fsum = 0
while True:
    x = fib(n)
    if x >= 4000000:
        break
    fsum += x if x % 2 == 0 else 0
    n = n + 1

print(fsum)
