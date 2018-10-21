import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

hours = int(line[0])
minutes = int(line[1])

minutes -= 45

if minutes < 0:
    hours = (hours - 1) % 24
    minutes = 60 + minutes

print(hours, minutes)
