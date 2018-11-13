import sys

number = sys.stdin.readline()

while number:
    number = int(number)
    factors = []
    factor = 2

    x = number

    while x >= factor**2:

        if x % factor == 0:
            x = x / factor
            factors.append(factor)
        else:
            factor += 1

    factors.append(int(x))

    bases = []
    exp = []

    for factor in factors:
        if factor not in bases:
            bases.append(factor)
            exp.append(1)
        else:
            index = bases.index(factor)
            exp[index] += 1

    divisors = []
    for i in range(exp[0] + 1):
        divisors.append(bases[0] ** i)

    until = len(divisors) - 1

    for i in range(1, len(bases)):
        for k in range(exp[i] + 1):
            j = 0
            while j <= until:
                result = divisors[j] * bases[i] ** k
                if result not in divisors:
                    divisors.append(result)
                j += 1
            if k == exp[i]:
                until = len(divisors) - 1

    divisors.remove(number) 

    count = 0

    for divisor in divisors:
        count += divisor
    
    if count == number:
        print('%d perfect' % number)
    elif count >= number - 2 and count <= number + 2:
        print('%d almost perfect' % number)
    else:
        print('%d not perfect' % number)

    number = sys.stdin.readline()
