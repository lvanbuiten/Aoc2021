from __future__ import annotations

import collections
from pathlib import Path
from dataclasses import dataclass
import time
import sys
from typing import Generator
from queue import PriorityQueue

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = inputFile.read().splitlines()

coords = collections.defaultdict(lambda: -1)

for x, line in enumerate(input):
    for y, char in enumerate(line):
        coords[(x, y)] = int(char)

lowestRisk = sys.maxsize

@dataclass
class Point:
    x: int
    y: int
    value: int
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
  
def adjacent(x: int, y: int) -> Generator[tuple[int, int], None, None]:
    yield x - 1, y # above
    yield x, y - 1 # left
    yield x, y + 1 # right
    yield x + 1, y # below

'''visited[] keeps track of vertices in current path.
path[] stores actual vertices and path_index is current
index in path[]'''
def findAllPathsUtil(c: Point, visited, path, risk):
    # Mark the current node as visited and store in path
    visited[f'({c.x},{c.y})'] = True
    path.append(c)

    # If current vertex is same as destination, then print
    # current path[]
    global lowestRisk
    if c == destination:
        if risk < lowestRisk:
            lowestRisk = risk
        #print (path)
    # not going to improve on this path if current risk is already higher then lowestRisk
    elif risk < lowestRisk:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for p in adjacent(c.x, c.y):
            x = p[0]
            y = p[1]
            val = coords.get(p, -1)
            if val != -1 and visited[f'({x},{y})'] == False:
                point = Point(x, y, val)
                findAllPathsUtil(point, visited, path, risk+val)
                    
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[f'({c.x},{c.y})'] = False

# Find all paths
def findAllPaths():
    # Mark all the vertices as not visited
    visited = {}
    global coords
    for k in coords.keys():
        visited[f'({k[0]},{k[1]})'] = False

    # Create an array to store paths
    start = Point(0, 0, 0)
    path = []
    risk = 0

    # Call the recursive helper function to print all paths
    findAllPathsUtil(start, visited, path, risk)


endX = len(input)-1
endY = len(input[0])-1
destination = Point(endX, endY, coords.get((endX, endY)))

print("Following are all different paths from start to end:")
findAllPaths()
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
