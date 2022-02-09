from __future__ import annotations

from collections import Counter
from collections import defaultdict
from pathlib import Path
from dataclasses import dataclass
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = inputFile.read().splitlines()

answer = 0

class Graph:
  
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an two way edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
  
    '''A recursive function to print all paths from 'u' to 'd' and path[] stores actual vertices'''
    def printAllPathsUtil(self, u, d, path):
 
        # Mark the current node as visited and store in path
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            global answer
            answer += 1
            print(','.join(path))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            notHadSingleSmallCave = len([p for p in path if p == str.lower(p) and path.count(p) >= 2]) == 0
            for i in self.graph[u]:
                if i == 'start':
                    continue
                elif str.isupper(i) or i not in path:
                    self.printAllPathsUtil(i, d, path)
                elif notHadSingleSmallCave and path.count(i) == 1:
                    self.printAllPathsUtil(i, d, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d): 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, path)


g = Graph()

for i in input:
    s, e = i.split('-')
    g.addEdge(s, e)

print("Following are all different paths from start to end:")
g.printAllPaths('start', 'end')
print('')

print(f"Done! Answer is '{answer}' for question Given these new rules, how many paths through this cave system are there?, --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---

# After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

# Now, the 36 possible paths through the first example above are:

# start,A,b,A,b,A,c,A,end
# start,A,b,A,b,A,end
# start,A,b,A,b,end
# start,A,b,A,c,A,b,A,end
# start,A,b,A,c,A,b,end
# start,A,b,A,c,A,c,A,end
# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,d,b,A,c,A,end
# start,A,b,d,b,A,end
# start,A,b,d,b,end
# start,A,b,end
# start,A,c,A,b,A,b,A,end
# start,A,c,A,b,A,b,end
# start,A,c,A,b,A,c,A,end
# start,A,c,A,b,A,end
# start,A,c,A,b,d,b,A,end
# start,A,c,A,b,d,b,end
# start,A,c,A,b,end
# start,A,c,A,c,A,b,A,end
# start,A,c,A,c,A,b,end
# start,A,c,A,c,A,end
# start,A,c,A,end
# start,A,end
# start,b,A,b,A,c,A,end
# start,b,A,b,A,end
# start,b,A,b,end
# start,b,A,c,A,b,A,end
# start,b,A,c,A,b,end
# start,b,A,c,A,c,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,d,b,A,c,A,end
# start,b,d,b,A,end
# start,b,d,b,end
# start,b,end

# The slightly larger example above now has 103 paths through it, and the even larger example now has 3509 paths through it.

# Given these new rules, how many paths through this cave system are there?
