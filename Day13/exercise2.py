from __future__ import annotations

import collections
from logging.config import dictConfig
from pathlib import Path
from dataclasses import dataclass
import numpy as np
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
values, operations = inputFile.read().split('\n\n')

inputCoords = collections.defaultdict(list)
xMax = yMax = 0

for v in values.split('\n'):
    yS,xS = v.split(',')
    x = int(xS)
    y = int(yS)

    xMax = x if x > xMax else xMax
    yMax = y if y > yMax else yMax

    inputCoords[x].append(y)

# y appearently +2 otherwise it doesn't work...
coords = [['.']*(yMax+2) for i in range(xMax+1)]

row = ["." for x in range(xMax+1)]
paper = []
for i in range(yMax + 2):
    paper.append([x for x in row])

def Count() -> int:
    result = 0
    for x, vals in enumerate(coords):
        for e in vals:
            if e == '#':
                result += 1
    return result


for ic in inputCoords:
    for k in inputCoords[ic]:
        coords[ic][k] = '#'

print(f"Input count {Count()}")

for o in operations.split('\n'):
    axis,index_s = o.replace('fold along ', '').split('=')
    index = int(index_s)
        
    if axis == "y":
        above = coords[:index]
        below = coords[index + 1:][::-1]
        diff = len(above) - len(below)
        for i in range(len(below)):
            for j in range(len(below[i])):
                if below[i][j] == "#":
                    above[diff+i][j] = "#"
        coords = above
    else:
        left = [[x for x in y[:index]] for y in coords]
        right = [[x for x in y[index + 1:][::-1]] for y in coords]
        diff = len(left) - len(right)
        for i in range(len(right)):
            for j in range(len(right[i])):
                if right[i][j] == "#":
                    left[diff+i][j] = "#"
        
        coords = left


# print
for x, vals in enumerate(coords):
    for e in vals:
        if e == '#':
            print('#', end='')
        else:
            print(' ', end='')
    print()

answer = 'ZKAUCFUC'
print(f"Done! Answer is '{answer}' for question What code do you use to activate the infrared thermal imaging camera system?, --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---

# Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

# What code do you use to activate the infrared thermal imaging camera system?
