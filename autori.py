import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split('-')

for word in line:
    print(word[0], end = '')

