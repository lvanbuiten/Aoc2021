from __future__ import annotations

from pathlib import Path
from typing import NamedTuple
import numpy as np
import re

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
# inputFile = re.split
# lines = inputFile.read().splitlines()

class Point(NamedTuple):
    start: set[int]
    end: set[int]
    
    @classmethod
    def parse(cls, line: str) -> Point:
        strTyples = line.split(" -> ")
        startValues = strTyples[0].split(',')
        start = [int(startValues[0]), int(startValues[1])]

        enValues = strTyples[1].split(',')
        end = [int(enValues[0]), int(enValues[1])]

        # Optimization 
        # startV, endV = line.split(" -> ")
        # x1_s, y1_s = startV.split(",")
        # x2_s, y2_s = endV.split(",")
        # start = [int(x1_s), int(y1_s)]
        # end = [int(x2_s), int(y2_s)]

        return cls(start, end)

points = [Point.parse(point) for point in inputFile.read().splitlines()]
coordinates = {}

for p in points:
    # horizontal
    if (p.start[0] == p.end[0]):
        x = p.start[0]
        y = p.start[1]

        # switch on looping forwards or backwards
        start = y if y <= p.end[1] else p.end[1]
        end = y if y >= p.end[1] else p.end[1]

        while (start <= end):
            value = coordinates[f'{x},{start}'] if f'{x},{start}' in coordinates else 0
            value += 1 
            coordinates[f'{x},{start}'] = value
            start += 1

        # Optimization 
        # for y in range(min(p.start[1], p.end[1]), max(p.start[1], p.end[1]) + 1):
        #     values = ...
        # using Counter (import collections), checking for key is not neccessary.

    # vertical
    elif (p.start[1] == p.end[1]):
        x = p.start[0]
        y = p.start[1]

        # switch on looping forwards or backwards
        start = x if x <= p.end[0] else p.end[0]
        end = x if x >= p.end[0] else p.end[0]

        while (start <= end):
            value = coordinates[f'{start},{y}'] if f'{start},{y}' in coordinates else 0
            value += 1 
            coordinates[f'{start},{y}'] = value
            start += 1
    # diagonal, so skip (for this exercise)
    else:
        continue


total = len([x for x in coordinates.values() if x > 1])
print(f"Done! Total amount of coordinates with at least two lines overlapping is '{total}'")

# --- Day 5: Hydrothermal Venture ---
# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2

# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:
#     An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#     An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.
# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....

# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
