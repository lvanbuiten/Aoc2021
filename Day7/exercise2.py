from __future__ import annotations

from collections import Counter
from pathlib import Path
from dataclasses import dataclass
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = [int(i) for i in inputFile.readline().split(',')]
counter = Counter(input)
# most_common = counter.most_common()
# middle = sum(input) / len(input)
# nearest = min(input, key=lambda x:abs(x-middle))
fuel = None
position = None
print(f'Initial state is: {input}')

# for key,val in most_common:

for c in range(max(input)):
    currentTotalFuel = 0
    for i in input:
        maxN = abs(i - c)
        currentTotalFuel += maxN * (maxN+1) / 2

    if (fuel == None or fuel > currentTotalFuel):
        fuel = currentTotalFuel
        position = c
        
print(f"Done! Least amount of fuel '{int(fuel)}' at position '{position}', --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---
# The crabs don't seem interested in your proposed solution. Perhaps you misunderstand crab engineering?
# As it turns out, crab submarine engines don't burn fuel at a constant rate. Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last: the first step costs 1, the second step costs 2, the third step costs 3, and so on.
# As each crab moves, moving further becomes more expensive. This changes the best horizontal position to align them all on; in the example above, this becomes 5:

#     Move from 16 to 5: 66 fuel
#     Move from 1 to 5: 10 fuel
#     Move from 2 to 5: 6 fuel
#     Move from 0 to 5: 15 fuel
#     Move from 4 to 5: 1 fuel
#     Move from 2 to 5: 6 fuel
#     Move from 7 to 5: 3 fuel
#     Move from 1 to 5: 10 fuel
#     Move from 2 to 5: 6 fuel
#     Move from 14 to 5: 45 fuel

# This costs a total of 168 fuel. This is the new cheapest possible outcome; the old alignment position (2) now costs 206 fuel instead.
# Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?
