import sys

limit = int(sys.stdin.readline())
n = int(sys.stdin.readline())

storage = 0

for i in range(n):
    usage = int(sys.stdin.readline())
    if usage < limit:
        storage += limit - usage
    else:
        storage -= usage - limit

print(storage + limit)
