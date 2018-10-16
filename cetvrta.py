import math, sys

points = []

point1 = sys.stdin.readline()
point1 = point1[:len(point1)-1].split(' ')
points.append(point1)
point2 = sys.stdin.readline()
point2 = point2[:len(point2)-1].split(' ')
points.append(point2)
point3 = sys.stdin.readline()
point3 = point3[:len(point3)-1].split(' ')
points.append(point3)

dictionary = {
    'x': {
        },
    'y': {
        }
    }

for point in points:
    if str(point[0]) in dictionary['x']:
        dictionary['x'][str(point[0])] += 1
    else:
        dictionary['x'][str(point[0])] = 1
    if str(point[1]) in dictionary['y']:
        dictionary['y'][str(point[1])] += 1
    else:
        dictionary['y'][str(point[1])] = 1

for key in dictionary['x']:
    if dictionary['x'][key] == 1:
        x = key

for key in dictionary['y']:
    if dictionary['y'][key] == 1:
        y = key

print(x, y)
                   

