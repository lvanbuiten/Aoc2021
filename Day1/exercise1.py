from pathlib import Path

# Using readlines()
inputFile = open(Path(__file__).with_name('exercise-input.txt'), 'r')
lines = inputFile.readlines()

lastValue = None
increasedCounter = int()

for line in lines:
    lineValue = int(line)
    if (lastValue != None and (lineValue - lastValue) > 0):
        increasedCounter = increasedCounter + 1
    lastValue = lineValue
    
print("Counter for increased values = " + str(increasedCounter))