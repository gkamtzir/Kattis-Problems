import math, sys
from operator import itemgetter

def price(p, a, b, c, d, k):
    return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2) 

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

p = int(line[0])
a = int(line[1])
b = int(line[2])
c = int(line[3])
d = int(line[4])
n = int(line[5])

max_price = 0.0
max_decline = 0.0

for i in range(1, n+1):
    current_price = price(p, a, b, c, d, i)
    if max_price - current_price > max_decline:
        max_decline = max_price - current_price
    if current_price > max_price:
        max_price = current_price
    
print('%.9f' % (max_decline))

