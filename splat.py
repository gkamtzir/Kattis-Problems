import math

def in_circle(center_x, center_y, x, y, radius):
    distance = (center_x - x) ** 2 + (center_y - y) ** 2
    return True if distance <= radius ** 2 else False

c = int(input())

for j in range(c):

    n = int(input())

    canvas = []

    for i in range(n):
        drop = input().split(' ')
        drop[2] = str(math.sqrt(float(drop[2])/math.pi))
        canvas.append(drop)

    canvas = canvas[::-1]

    m = int(input())

    for i in range(m):
        coord = list(map(float, input().split()))
        found = False
        for drop in canvas:
            if in_circle(float(drop[0]), float(drop[1]), coord[0], coord[1], float(drop[2])):
                print(drop[3])
                found = True
                break
        if not found:
            print('white')
