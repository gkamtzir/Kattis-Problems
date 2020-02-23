from decimal import *
import sys

getcontext().prec = 10000

for line in sys.stdin:
    a, b, c = map(int, line.split())

    result = str(Decimal(a) / Decimal(b))

    if len(result) < c + 2:
        result += "0" * (c + 2 - len(result))

    print(result[:c + 2])
