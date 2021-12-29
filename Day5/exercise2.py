from __future__ import annotations

from pathlib import Path
from typing import NamedTuple
import numpy as np
import re
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
# inputFile = re.split
# lines = inputFile.read().splitlines()

class Point(NamedTuple):
    xStart: int
    yStart: int
    xEnd: int
    yEnd: int
    
    @classmethod
    def parse(cls, line: str) -> Point:
        strTyples = line.replace(" -> ", ",")
        values = strTyples.split(',')
        xStart = int(values[0])
        yStart = int(values[1])
        xEnd = int(values[2])
        yEnd = int(values[3])

        return cls(xStart, yStart, xEnd, yEnd)

points = [Point.parse(point) for point in inputFile.read().splitlines()]
coordinates = {}

for p in points:
    # horizontal
    if (p.xStart == p.xEnd):
        x = p.xStart
        y = p.yStart

        # switch on looping forwards or backwards
        start = y if y <= p.yEnd else p.yEnd
        end = y if y >= p.yEnd else p.yEnd

        while (start <= end):
            value = (coordinates[f'{x},{start}']+1) if f'{x},{start}' in coordinates else 1
            coordinates[f'{x},{start}'] = value
            start += 1
    # vertical
    elif (p.yStart == p.yEnd):
        x = p.xStart
        y = p.yStart

        # switch on looping forwards or backwards
        start = x if x <= p.xEnd else p.xEnd
        end = x if x >= p.xEnd else p.xEnd

        while (start <= end):
            value = (coordinates[f'{start},{y}']+1) if f'{start},{y}' in coordinates else 1
            coordinates[f'{start},{y}'] = value
            start += 1
    # diagonal
    else:
        # top left to bottom right -> x and y will increase
        if ((p.xStart > p.xEnd and p.yStart > p.yEnd) or
            (p.xStart < p.xEnd and p.yStart < p.yEnd)):

            if (p.xStart > p.xEnd):
                xStart = p.xEnd                
                yStart = p.yEnd
                end = p.xStart
            else:
                xStart = p.xStart                
                yStart = p.yStart
                end = p.xEnd
            while (xStart <= end):
                value = (coordinates[f'{xStart},{yStart}']+1) if f'{xStart},{yStart}' in coordinates else 1
                coordinates[f'{xStart},{yStart}'] = value
                xStart += 1
                yStart += 1        
        # bottom left to top right -> x will increase, y will decrease
        else:
            if (p.xStart > p.xEnd):
                xStart = p.xEnd                
                yStart = p.yEnd
                end = p.xStart
            else:
                xStart = p.xStart                
                yStart = p.yStart
                end = p.xEnd
            while (xStart <= end):
                value = (coordinates[f'{xStart},{yStart}']+1) if f'{xStart},{yStart}' in coordinates else 1
                coordinates[f'{xStart},{yStart}'] = value
                xStart += 1
                yStart -= 1
            continue

total = len([x for x in coordinates.values() if x > 1])
print(f"Done! Total amount of coordinates with at least two lines overlapping is '{total}', --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---
# Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.
# Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

#     An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
#     An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

# Considering all lines from the above example would now produce the following diagram:

# 1.1....11.
# .111...2..
# ..2.1.111.
# ...1.2.2..
# .112313211
# ...1.2....
# ..1...1...
# .1.....1..
# 1.......1.
# 222111....

# You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.
# Consider all of the lines. At how many points do at least two lines overlap?
