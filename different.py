import sys

for line in sys.stdin:
    line = line[:len(line)-1].split(' ')
    print(abs(int(line[0]) - int(line[1])))


