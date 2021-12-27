from pathlib import Path
import numpy as np
import re

inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
# inputFile = re.split
lines = inputFile.read().splitlines()

boardSize = 5
possibleDraws = lines.pop(0).split(',')
drawnNumbers = possibleDraws[:boardSize-1] # grab first {boardSize}, because with {boardSize-1} you can't get bingo
del possibleDraws[:boardSize-1]

lines.pop(0) # remove first empty line
board = [None] * boardSize
boardIndex = flatboardIndex = 0
flatBoards = list()
currentDraw = winningBoard = ''
done = False

# build the boards to a flat array
for line in lines:
    if (line == ""):
        board = np.rot90(board)

        for b in board:
            flatBoards[flatboardIndex] += (",".join(b) + ";") # add columns to current flat board

        board = [None] * boardSize
        boardIndex = 0
        flatboardIndex += 1
        continue

    board[boardIndex] = re.findall('\d+', line)
    if len(flatBoards) <= flatboardIndex:
        flatBoards.append('')
    flatBoards[flatboardIndex] += (",".join(board[boardIndex]) + ";") # add rows to current flat board
    boardIndex += 1

for index, fb in enumerate(flatBoards):
    for d in drawnNumbers:
        fb = re.sub(f"(^|,|;)+{d}(,|;)+", "\g<1>x\g<2>", fb)
        flatBoards[index] = fb

def solved():
    for index, fb in enumerate(flatBoards):
        fb = re.sub(f"(^|,|;)+{currentDraw}(,|;)+", "\g<1>x\g<2>", fb)
        if (re.search('x,x,x,x,x;', fb)):
            global winningBoard, done
            winningBoard = fb[:[i for i, n in enumerate(fb) if n == ';'][boardSize-1]]
            done = True
            return True
        flatBoards[index] = fb
    return False

while (solved() == False):
    if (len(possibleDraws) == 0):
        print("Damn it's unsolvable...")
        break

    # for index, fb in enumerate(flatBoards):
    #     fb = re.sub(f"(^|,|;)+{currentDraw}(,|;)+", "\g<1>x\g<2>", fb)
    #     if (re.search('x,x,x,x,x;', fb)):
    #         winningBoard = fb[:[i for i, n in enumerate(fb) if n == ';'][boardSize-1]]
    #         done = True
    #         break
    #     flatBoards[index] = fb

    if done:
        break

    currentDraw = possibleDraws.pop(0)
    drawnNumbers.append(currentDraw)

sumofboard = sum(np.asarray(re.findall('\d+', winningBoard)).astype(int))
print(f"Done! Sum of board is {sumofboard} multiplied with last drawn vale {currentDraw} makes {sumofboard*int(currentDraw)}")  


# --- Day 4: Giant Squid ---
# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.
# Maybe it wants to play bingo?
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:
# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7

# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# Finally, 24 is drawn:
# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).
# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.
# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
