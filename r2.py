import sys

line = sys.stdin.readline()
line = line[:len(line) -1].split(' ')

print(int(line[1]) * 2 - int(line[0]))
