N, L = map(int, input().split())

time = 0
prev = 0

for i in range(N):
    D, R, G = map(int, input().split())
    time += D - prev
    prev = D
    test = time % (R + G)
    if test == 0:
        test += 1
    if test < R:
        time += R - test

time += L - prev

print(time)
    
