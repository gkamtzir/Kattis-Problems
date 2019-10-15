import sys

maximum_length = -1
lengths = []

# Reading user input.
for line in sys.stdin:
    line = line[:len(line) - 1]
    
    # Storing the lengths.
    lengths.append(len(line))

    # Storing the maximum length.
    if len(line) > maximum_length:
        maximum_length = len(line)

# Removing the last element.
lengths.pop()

score = 0

# Calculating the score.
for length in lengths:
    score += (maximum_length - length) ** 2

print(score)

