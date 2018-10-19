import sys

#It's prime factorization
x = int(sys.stdin.readline())

k = 0

factor = 2

while x >= factor**2:

    if x % factor == 0:
        x = x / factor
        k += 1
    else:
        factor += 1

k += 1

print(k)
