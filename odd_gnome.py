import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split(' ')
    line = line[1:]
    before = int(line[0]) - 1
    for index in range(len(line)):
        if before + 1 != int(line[index]):
            print(index + 1)
            break
        before += 1
