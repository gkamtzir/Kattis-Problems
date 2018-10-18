import sys

pawn_list = [1, 1, 2, 2, 2, 8]

line = sys.stdin.readline()
line = line[:len(line) -1].split(' ')

for index in range(len(line)):
    print(pawn_list[index] - int(line[index]), end = ' ')
