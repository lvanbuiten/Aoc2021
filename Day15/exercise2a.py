from __future__ import annotations

import sys
import collections
from pathlib import Path
from dataclasses import dataclass
import time
import sys
from typing import Generator
import heapq

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = inputFile.read().splitlines()

coords = {}

for i in range(5):
    for x, line in enumerate(input):
        for j in range(5):
            for y, char in enumerate(line):
                val = int(char) + j + i
                if val > 9:
                    val = val % 9
                coords[(x+(i*len(input)), y+(j*len(line)))] = val

def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y # above
    yield x, y - 1 # left
    yield x, y + 1 # right
    yield x + 1, y # below

def dijkstra(final_x: int, final_y: int, coords: dict) -> int:
    best_at: dict[tuple[int, int], int] = {}

    todo = [(0, (0, 0))]
    while todo:
        cost, last_coord = heapq.heappop(todo)

        # update our costs
        if last_coord in best_at and cost >= best_at[last_coord]:
            continue
        else:
            best_at[last_coord] = cost
        
        # we are there
        if last_coord == (final_x, final_y):
            return cost
        
        # continue our path
        for neighbour in adjacent(*last_coord):
            if neighbour in coords:
                heapq.heappush(todo, (cost + coords[neighbour], neighbour))

    return best_at[(final_x, final_y)]

endX, endY = max(coords)
lowestRisk = dijkstra(endX, endY, coords) 
print('')

print(f"Done! Answer is '{lowestRisk}' for question What is the lowest total risk of any path from the top left to the bottom right?, --- {(time.time() - start_time)} seconds ---")

# --- Day 15: Chiton ---

# You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

# The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581

# You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

# Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581

# The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

# What is the lowest total risk of any path from the top left to the bottom right?
