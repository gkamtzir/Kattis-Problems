r, n = map(int, input().split())

booked = []

for i in range(n):
    booked.append(int(input()))

if n == r:
    print('too late')
else:
    i = 1
    while i <= r:
        if i not in booked:
            print(i)
            break
        i += 1
