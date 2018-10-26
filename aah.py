import sys

line = sys.stdin.readline()
marius = line[:len(line) - 1]

line = sys.stdin.readline()
doctor = line[:len(line) - 1]

print('go' if len(marius) >= len(doctor) else 'no')
