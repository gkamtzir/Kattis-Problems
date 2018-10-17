import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

print((int(line[1]) - 1) * int(line[0]) + 1)

