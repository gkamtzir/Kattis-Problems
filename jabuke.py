# Returns the line formula and the 'direction'
# of the third point of the vertex.
def find_line(x1, y1, x2, y2, x3, y3):
    slope = (y2 - y1)/(x2 - x1)
    b = -slope * x1 + y1
    result = slope * x3 + b
    if result < y3:
        direction = "greater"
    else:
        direction = "less"
    return {
        "slope": slope,
        "b": (-slope * x1 + y1),
        "direction": direction
        }

# Checks if a point is on the right or left
# of the given line.
def in_triangle(slope, b, direction, x, y):
    result = slope * x + b
    if direction == "greater":
        if y >= result:
            return True
        else:
            return False
    else:
        if y <= result:
            return True
        else:
            return False

# Calculates the are of the triangle
# that the three points create.
def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
  
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

N = int(input())

triangle = []

triangle.append(find_line(x1, y1, x2, y2, x3, y3))
triangle.append(find_line(x2, y2, x3, y3, x1, y1))
triangle.append(find_line(x1, y1, x3, y3, x2, y2))

count = 0

for i in range(N):
    x, y = map(int, input().split())
    count += 1
    for line in triangle:
        if not in_triangle(line["slope"], line["b"], line["direction"], x, y):
            count -= 1
            break

print(calculate_area(x1, y1, x2, y2, x3, y3))
print(count)
