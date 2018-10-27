import math, sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
B = int(line[0])
Br = int(line[1])
Bs = int(line[2])
A = int(line[3])
As = int(line[4])

Bobs_money = (Br - B) * Bs

answer = A + Bobs_money / As

if int(answer) == answer:
    answer = int(answer) + 1
else:
    answer = math.ceil(answer)

print(answer)
