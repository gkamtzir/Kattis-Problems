import sys

def factorial(n):
    if n > 10:
        return 1000000
    if n == 1 or n == 2:
        return n
    else:
        return n*factorial(n-1)
        
number = int(sys.stdin.readline())

if number > 10:
    number = 10

probability = 0.0

for i in range(1, number+1):
    probability += (-1)**(i+1) * 1 / factorial(i)

print('%.9f' % probability)
