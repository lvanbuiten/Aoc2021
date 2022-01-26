from __future__ import annotations

from collections import Counter
from pathlib import Path
from dataclasses import dataclass
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = [list(map(int,l)) for l in inputFile.read().splitlines()]


print(f'Initial state is: {input}')
values = []
for i, row in enumerate(input):
    for j, curVal in enumerate(row):
        # edge top
        if i == 0:
            if curVal >= input[i+1][j]:
                continue
        # edge bottom
        elif i == len(input)-1:
            if curVal >= input[i-1][j]:
                continue
        elif curVal >= input[i+1][j] or curVal >= input[i-1][j]:
            continue

        # edge left
        if j == 0:
            if curVal >= input[i][j+1]:
                continue
        # edge right
        elif j == len(row)-1:
            if curVal >= input[i][j-1]:
                continue
        elif curVal >= input[i][j+1] or curVal >= input[i][j-1]:
            continue
    
        values.append(curVal)
        

answer = sum([x+1 for x in values])
        
print(f"Done! Answer is '{answer}' for question What is the sum of the risk levels of all low points on your heightmap?, --- {(time.time() - start_time)} seconds ---")


# --- Day 9: Smoke Basin ---

# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.
# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).
# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.
# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)
# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.
# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.
# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?
