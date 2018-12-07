T = int(input())

for i in range(T):
    P, R, F = map(int, input().split())
    result = 0
    while True:
        if P > F:
            print(result)
            break
        P *= R
        result += 1
