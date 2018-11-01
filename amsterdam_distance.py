import math, sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

M = int(line[0])
N = int(line[1])
R = float(line[2])

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
line = [int(x) for x in line]

a_x = line[0]
a_y = line[1]
b_x = line[2]
b_y = line[3]

total_distance = 0.0

if a_y > b_y:
    total_distance += abs(a_y - b_y) * (1/N) * R
    angle = abs(a_x - b_x) * (math.pi / M)
    if angle > 2.0:
        total_distance += 2 * b_y * (1/N) * R
    else:
        total_distance += angle * b_y * (1/N) * R
elif a_y < b_y:
    angle = abs(a_x - b_x) * (math.pi / M)
    if angle > 2.0:
        total_distance += 2 * a_y * (1/N) * R
    else:
        total_distance += angle * a_y * (1/N) * R
    total_distance += abs(a_y - b_y) * (1/N) * R
else:
    angle = abs(a_x - b_x) * (math.pi / M)
    if angle > 2.0:
        total_distance += 2 * a_y * (1/N) * R
    else:
        total_distance += angle * a_y * (1/N) * R

print('%.14f' % total_distance)
