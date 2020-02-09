def in_circle(x, y, radius, x1, y1):
    return (x - x1) ** 2 + (y - y1) ** 2 <= radius ** 2

def in_rectangular(x1, y1, x2, y2, x, y):
    return x >= x1 and x <= x2 and y >= y1 and y <= y2

m = int(input())

shapes = []

for i in range(m):
    shapes.append(input().split())

n = int(input())

for i in range(n):
    count = 0
    x, y = map(int, input().split())
    for shape in shapes:
        if shape[0] == "rectangle" and in_rectangular(int(shape[1]), int(shape[2]), int(shape[3]), int(shape[4]), x, y):
            count += 1
        elif shape[0] == "circle" and in_circle(int(shape[1]), int(shape[2]), int(shape[3]), x, y):
            count += 1
    print(count)
    
