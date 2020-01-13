import math

h, u = map(int, input().split())

length = h / math.sin(u * math.pi / 180)

print(math.ceil(length))
