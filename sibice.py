import math, sys

line = sys.stdin.readline()
line = line[:len(line)-1].split(' ')

number_of_matches = int(line[0])
x = int(line[1])
y = int(line[2])

max_length = math.sqrt(x**2 + y**2)
outputs = []

for match in range(number_of_matches):
    match_length = int(sys.stdin.readline())
    if match_length <= max_length:
        outputs.append('DA')
    else:
        outputs.append('NE')

for output in outputs:
    print(output)


