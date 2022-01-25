from __future__ import annotations

from collections import Counter
from pathlib import Path
from dataclasses import dataclass
import time

start_time = time.time()

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
input = inputFile.readlines()


print(f'Initial state is: {input}')


def resolveInput(input:str) -> int:
    left, right = input.split(' | ')

    values = {}

    x1, = ["".join(sorted(l)) for l in left.split() if len(l) == 2] # 1
    values[x1] = 1
    x4, = ["".join(sorted(l)) for l in left.split() if len(l) == 4] # 4
    values[x4] = 4
    x7, = ["".join(sorted(l)) for l in left.split() if len(l) == 3] # 7
    values[x7] = 7
    x8, = ["".join(sorted(l)) for l in left.split() if len(l) == 7] # 8
    values[x8] = 8
    
    # length of 6
    x9, = ["".join(sorted(l)) for l in left.split() if len(l) == 6 and all(elem in l for elem in sorted(x4))] # 9
    values[x9] = 9
    x, = ["".join(sorted(l)) for l in left.split() if len(l) == 6 and "".join(sorted(l)) not in values and all(elem in l for elem in sorted(x7))] # 0
    values[x] = 0
    x, = ["".join(sorted(l)) for l in left.split() if len(l) == 6 and "".join(sorted(l)) not in values] # 6
    values[x] = 6

    # length of 5 
    x, = ["".join(sorted(l)) for l in left.split() if len(l) == 5 and all(elem in l for elem in sorted(x1))] # 3
    values[x] = 3
    x, = ["".join(sorted(l)) for l in left.split() if len(l) == 5 and "".join(sorted(l)) not in values and all(elem in sorted(x9) for elem in l)] # 5
    values[x] = 5
    x, = ["".join(sorted(l)) for l in left.split() if len(l) == 5 and "".join(sorted(l)) not in values] # 2
    values[x] = 2

    answer = ''
    for r in right.split():
        answer += str(values["".join(sorted(r))])


    # optimaliztion
    # see: https://www.youtube.com/watch?v=WDFh2jdUYlw
    # sort left and right at the start
    # use set() instead of sorted to 'split' on character

    # search for left hand side first where len() == 6 (for example)
    # and the last value can be solved by 'set of 6' - {numberX, numberY}

    return int(answer)

answer = sum([resolveInput(x) for x in input])
        
print(f"Done! Answer is '{answer}' for question What do you get if you add up all of the output values?, --- {(time.time() - start_time)} seconds ---")

# --- Part Two ---

# Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf
# After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

# So, the unique signal patterns would correspond to the following digits:
#     acedgfb: 8
#     cdfbe: 5
#     gcdfa: 2
#     fbcad: 3
#     dab: 7
#     cefabd: 9
#     cdfgeb: 6
#     eafb: 4
#     cagedb: 0
#     ab: 1

# Then, the four digits of the output value can be decoded:
#     cdfeb: 5
#     fcadb: 3
#     cdfeb: 5
#     cdbaf: 3

# Therefore, the output value for this entry is 5353.
# Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

#     fdgacbe cefdb cefbgd gcbe: 8394
#     fcgedb cgb dgebacf gc: 9781
#     cg cg fdcagb cbg: 1197
#     efabcd cedba gadfec cb: 9361
#     gecf egdcabf bgf bfgea: 4873
#     gebdcfa ecba ca fadegcb: 8418
#     cefg dcbef fcge gbcadfe: 4548
#     ed bcgafe cdgba cbgef: 1625
#     gbdfcae bgc cg cgb: 8717
#     fgae cfgab fg bagce: 4315

# Adding all of the output values in this larger example produces 61229.
# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?
