import sys

line = sys.stdin.readline()
line = line[:len(line) - 1]

i = 0
result = []

while i < len(line):
    if line[i] == '<':
        if len(result) > 0:
            result.pop()
    else:
        result.append(line[i])
    i += 1
print(''.join(result))
