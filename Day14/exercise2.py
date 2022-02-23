from __future__ import annotations

import collections
from pathlib import Path
from dataclasses import dataclass
from typing import Counter
import numpy as np
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input, pairs_s = inputFile.read().split('\n\n')

pairs = {}
for p in pairs_s.split('\n'):
    key, value = p.split(' -> ')
    pairs[key] = value

values = Counter()
for i in range(0, len(input)-1):
    values[input[i:i+2]] += 1

# 1 less then requested, because of next iterator
for i in range(39):
    new_values = Counter()

    for k,v in values.items():
        result = pairs[k]
        new_values[k[0] + result] += v
        new_values[result + k[1]] += v

    values = new_values


value_counter = Counter()
for k,v in values.items():
    value_counter[k[0]] += v
    value_counter[pairs[k]] += v

# add missing last char count
value_counter[input[-1]] += 1

most_common = value_counter.most_common()[0][1]
least_common = value_counter.most_common()[-1][1]
answer = most_common - least_common
print(f"Done! Answer is '{answer}' for question What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?, --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---

# The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

# In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

# Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
