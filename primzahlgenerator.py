#!/usr/bin/env python

# from random import randint


max = 99
integers = range(2, max)
prims = []

for i in integers:
    y = 2
    while y < i:
        if i % y == 0:
            y = 1
            break
        else:
            y += 1
            prims.append(i)

for i in prims:
    print i,
