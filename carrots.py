import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

for i in range(int(line[0])):
    sys.stdin.readline()

print(line[1])

