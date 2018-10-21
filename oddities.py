import sys

n = int(sys.stdin.readline())

for i in range(n):
    number = int(sys.stdin.readline())
    print(str(number) + ' is even' if number % 2 == 0 else str(number) + ' is odd')
