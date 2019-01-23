import sys, math

def check_if_inside_area(r, x, y):
    return x**2 + y**2 <= r**2

def calculate_distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

line = sys.stdin.readline()

while line:
    line = line[:len(line) - 1].split(" ")
    r, x, y = map(float, line)

    distance = calculate_distance_from_origin(x, y)

    if not check_if_inside_area(r, x, y):
        print("miss")
    else:
        theta = math.acos(distance/r)
        base = math.sqrt(r**2 - distance**2)
        sector_area = theta * r**2
        triangle_area = base * distance
        chord_area = sector_area - triangle_area
        distances = [math.pi * r**2 - chord_area, chord_area]
        print("%.6f %.6f" % (max(distances), min(distances)))
    
    line = sys.stdin.readline()
