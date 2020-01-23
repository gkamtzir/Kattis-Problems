a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

y_dist = abs(b - d)
x_dist = abs(a - c)

total = x_dist + y_dist

if t - total < 0:
    print("N")
elif (t - total) % 2 == 0:
    print("Y")
else:
    print("N")
