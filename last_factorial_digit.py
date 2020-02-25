import math

T = int(input())

for i in range(T):
    N = int(input())
    result = str(math.factorial(N))[-1:]
    print(result)
