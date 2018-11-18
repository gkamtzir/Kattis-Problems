import math

d, s = map(int, input().split())

upper, lower = 10000000000, 0.00000001

while upper - lower > 0.0000000001:
    mid = (upper + lower) / 2
    if mid + s < mid * math.cosh(d/(2 * mid)):
        lower = mid
    else:
        upper = mid

print(2 * mid * math.sinh(d/(2 * mid)))
