import sys

n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    line = line[:len(line) - 1]
    line = [int(x) for x in line]
    for index in range(len(line) - 2, -1, -2):
        result = line[index] * 2
        if result > 9:
            units = (result % 10)
            result = units + 1
        line[index] = result
    total = 0
    for number in line:
        total += number
    if total % 10 == 0:
        print('PASS')
    else:
        print('FAIL')
