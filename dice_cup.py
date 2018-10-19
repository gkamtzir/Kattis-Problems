import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

dice_1 = int(line[0])
dice_2 = int(line[1])

max_count = 1

mapper = {}

for i in range(1, dice_1 + 1):
    for j in range(1, dice_2 + 1):
        total = i + j
        if str(total) in mapper:
            mapper[str(total)] += 1
            if mapper[str(total)] > max_count:
                max_count = mapper[str(total)]
        else:
            mapper[str(total)] = 1

for key in mapper:
    if mapper[key] == max_count:
        print(key)
