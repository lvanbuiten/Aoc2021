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

    board[boardIndex] = line.split()
    if len(flatBoards) <= flatboardIndex:
        flatBoards.append('')
    flatBoards[flatboardIndex] += (",".join(board[boardIndex]) + ";") # add rows to current flat board
    boardIndex += 1

for index, fb in enumerate(flatBoards):
    for d in drawnNumbers:
        fb = re.sub(f"(^|,|;)+{d}(,|;)+", "\g<1>x\g<2>", fb)
        flatBoards[index] = fb

def solved():
    index = 0
    while index < len(flatBoards):
        fb = flatBoards[index]
        fb = re.sub(f"(^|,|;)+{currentDraw}(,|;)+", "\g<1>x\g<2>", fb)
        flatBoards[index] = fb

        if (re.search('x,x,x,x,x;', fb)):
            del flatBoards[index]

            global winningBoard, done
            if (len(flatBoards) == 0):
                winningBoard = fb[:[i for i, n in enumerate(fb) if n == ';'][boardSize-1]]
                done = True
                return True
        else:
            index += 1
    return False

while (solved() == False):
    if (len(possibleDraws) == 0):
        print("Damn it's unsolvable...")
        break

    if done:
        break

    currentDraw = possibleDraws.pop(0)
    drawnNumbers.append(currentDraw)

sumofboard = sum(np.asarray(re.findall('\d+', winningBoard)).astype(int))
print(f"Done! Sum of board is {sumofboard} multiplied with last drawn vale {currentDraw} makes {sumofboard*int(currentDraw)}")  


# --- Part Two ---
# On the other hand, it might be wise to try a different strategy: let the giant squid win.
# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.
# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.
# Figure out which board will win last. Once it wins, what would its final score be?
