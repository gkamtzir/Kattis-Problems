import math

T = int(input())

for i in range(T):
    P, R, F = map(int, input().split())
    if P > F:
        print(0)
        continue
    result = math.log(F*R/P)/math.log(R)
    print(math.floor(result))
