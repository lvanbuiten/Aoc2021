from __future__ import annotations

from typing import NamedTuple
from collections import Counter
from pathlib import Path
from dataclasses import dataclass
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = [list(map(int,l)) for l in inputFile.read().splitlines()]

xMax = len(input)-1
yMax = len(input[0])-1

@dataclass
class Point:
    x: int
    y: int
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    # @classmethod
    def size(self, seen: list, input: list[list[int]]) -> int:
        myNB = []

        if self.x < xMax:
            if input[self.x+1][self.y] != 9:
                p = Point(self.x+1, self.y)
                if p not in seen:
                    myNB.append(p)
        if self.x > 0:
            if input[self.x-1][self.y] != 9:
                p = Point(self.x-1, self.y)
                if p not in seen:
                    myNB.append(p)
        if self.y < yMax:
            if input[self.x][self.y+1] != 9:
                p = Point(self.x, self.y+1)
                if p not in seen:
                    myNB.append(p)
        if self.y > 0:
            if input[self.x][self.y-1] != 9:
                p = Point(self.x, self.y-1)
                if p not in seen:
                    myNB.append(p)

        if len(myNB) == 0:
            return 1
        else:
            value = 1 # 1 for current
            seen.extend(myNB) # add all current Neighbours to seen
            for m in myNB:
                value += m.size(seen, input) # add value of all neighbours
            return value


print(f'Initial state is: {input}')
lowPoints = []
for i, row in enumerate(input):
    for j, curVal in enumerate(row):
        # edge top
        if i == 0:
            if curVal >= input[i+1][j]:
                continue
        # edge bottom
        elif i == xMax:
            if curVal >= input[i-1][j]:
                continue
        elif curVal >= input[i+1][j] or curVal >= input[i-1][j]:
            continue

        # edge left
        if j == 0:
            if curVal >= input[i][j+1]:
                continue
        # edge right
        elif j == yMax:
            if curVal >= input[i][j-1]:
                continue
        elif curVal >= input[i][j+1] or curVal >= input[i][j-1]:
            continue
    
        lowPoints.append(Point(i, j))


basin = []
for p in lowPoints:
    basin.append(p.size([p], input))


basin.sort(reverse=True)
answer = basin[0] * basin[1] * basin[2]

print(f"Done! Answer is '{answer}' for question What do you get if you multiply together the sizes of the three largest basins?, --- {(time.time() - start_time)} seconds ---")


# --- Part Two ---

# Next, you need to find the largest basins so you know what areas are most important to avoid.
# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.
# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
# The top-left basin, size 3:
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The top-right basin, size 9:
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The middle basin, size 14:
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The bottom-right basin, size 9:
# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.
# What do you get if you multiply together the sizes of the three largest basins?
