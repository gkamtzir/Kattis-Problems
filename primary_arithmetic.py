import sys

def output_message(total_carries):
    if total_carries == 0:
        return 'No carry operation.'
    elif total_carries == 1:
        return '1 carry operation.'
    else:
        return str(total_carries) + ' carry operations.'

outputs = []

while True:

    line = sys.stdin.readline()
    line = line[:len(line) - 1].split(' ')

    x = int(line[0])
    y = int(line[1])

    if x == 0 and y == 0:
        break

    mod = 10
    carry = 0
    total_carries = 0

    while True:
        x_1 = x % mod
        y_1 = y % mod

        if x == 0 and y == 0:
            break

        if x_1 + y_1 + carry >= 10:
            carry = 1
            total_carries += 1
        else:
            carry = 0

        x = int(x / mod)
        y = int(y / mod)
        
    outputs.append(output_message(total_carries))

for output in outputs:
    print(output)
