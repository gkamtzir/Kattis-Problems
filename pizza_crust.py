import math

R, C = map(int, input().split())

result = (math.pi * (R - C)**2)/(math.pi * R**2) * 100

print('%.6f' % result)
