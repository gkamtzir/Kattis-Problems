import sys

#We don't need the first value
line = sys.stdin.readline()

line = sys.stdin.readline()
temps = line[:len(line) - 1].split(' ')

count = 0

for temp in temps:
    if int(temp) < 0:
        count += 1

print(count)
