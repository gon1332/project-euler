#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(sum(x for x in range(3, 1000) if x % 3 == 0 or x % 5 == 0))
