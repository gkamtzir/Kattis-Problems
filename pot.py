import sys

n = int(sys.stdin.readline())

result = 0

for i in range(n):
    number = int(sys.stdin.readline())
    power = number % 10
    number = int(number / 10)
    result += number ** power

print(result)
