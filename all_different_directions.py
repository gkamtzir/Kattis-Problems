import math

def deg_to_rad(degrees):
    return (math.pi / 180) * degrees

def calculate_move(x, y, direction, instruction, value):
    if instruction == "walk":
        x = x + value * math.cos(deg_to_rad(direction))
        y = y + value * math.sin(deg_to_rad(direction))
    else:
        direction = direction + value
    return x, y, direction

def average_destination(points):
    x = 0
    y = 0
    for point in points:
        x += point[0]
        y += point[1]
    return x/len(points), y/len(points)

def find_worst_destination(points, average):
    worst = -1
    for point in points:
        distance = (point[0] - average[0]) ** 2 + (point[1] - average[1]) ** 2
        if distance > worst:
            worst = distance
    return math.sqrt(worst)
    
n = int(input())

while n != 0:
    points = []
    for _ in range(n):
        data = input().split()
        x, y = map(float, data[0:2])
        direction = float(data[3])
        instructions = data[4:]
        for i in range(0, len(instructions), 2):
            x, y, direction = calculate_move(x, y, direction, instructions[i], float(instructions[i + 1]))
        points.append([x, y])
    average_x, average_y = average_destination(points)
    worst = find_worst_destination(points, [average_x, average_y])
    print(f"{average_x} {average_y} {worst}")
    
    n = int(input())
