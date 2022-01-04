from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass
import time
import numpy as np

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = inputFile.readline()
# inputFile = re.split
# lines = inputFile.read().splitlines()

print(f'Initial state is: {input}')

@dataclass
class FishGroup:
    daysLeft: int
    counter: int

    # @classmethod
    def tickDay(self, fishGroupList: list[FishGroup]):
        if (self.daysLeft == 0):
            self.daysLeft = 6

            fishGroupList.append(FishGroup(8, self.counter))
        else:
            self.daysLeft += -1
            
        

values = np.array(input.split(','))
uniques, counts = np.unique(values, return_counts=True)
fishList = [FishGroup(int(uniques[x]), int(counts[x])) for x in range(len(uniques))]

def zipFishList(fishGroupList: list[FishGroup]) -> list[FishGroup]:
    newFishList: list[FishGroup] = []

    for f in fishGroupList:
        existingItems = [x for x in newFishList if x.daysLeft == f.daysLeft]
        if (len(existingItems) > 0):
            existingItems[0].counter += f.counter
        else:
            newFishList.append(f)

    return newFishList

 
# for i, unique in enumerate(uniques):
#     fishList = [FishGroup(int(unique), int(counts[i]))]
for x in range(1, 257):
    print(f"Currently at day '{x}'")
    if (x % 8 == 0):
        fishList = zipFishList(fishList)

    for f in fishList[:]:
        f.tickDay(fishList)

totalFishes = sum(f.counter for f in fishList)
print(f"Done! Total amount of fishes is '{totalFishes}', --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
# After 256 days in the example above, there would be a total of 26984457539 lanternfish!
# How many lanternfish would there be after 256 days?
