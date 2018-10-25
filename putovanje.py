import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

n = int(line[0])
capacity = int(line[1])

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
weights = [int(x) for x in line]

max_score = 0

for i in range(len(weights)):
    if len(weights) - i< max_score:
        break
    stomach = 0
    score = 0
    for index in range(i, len(weights)):
        if stomach + weights[index] <= capacity:
            stomach += weights[index]
            score += 1
        if stomach == capacity:
            break

    if score > max_score:
        max_score = score

print(max_score)
