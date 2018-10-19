import sys

m = int(sys.stdin.readline())

max_bus_number = 0
breaks = 0

memory = {}

for x in range(1, 100000):

    for y in range(x, 100000):

        total = x**3 + y**3

        if total > m:
            breaks += 1
            break

        if str(total) in memory:
            memory[str(total)] += 1
            if total > max_bus_number:
                max_bus_number = total
        else:
            memory[str(total)] = 1

if max_bus_number == 0:
    print('none')
else:
    print(max_bus_number)
