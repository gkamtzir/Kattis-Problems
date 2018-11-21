def calculate_distance_square(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

x, y = map(int, input().split())
point1 = [x, y]

x, y = map(int, input().split())
point2 = [x, y]

x, y = map(int, input().split())
point3 = [x, y]

dist_1_2 = calculate_distance_square(point1, point2)
dist_1_3 = calculate_distance_square(point1, point3)

if dist_1_2 == dist_1_3:
    temp = point1[:]
    point1 = point3[:]
    point3 = temp[:]
elif dist_1_3 > dist_1_2:
    temp = point2[:]
    point2 = point3[:]
    point3 = temp[:]

x = point1[0] + (point2[0] - point3[0])
y = point1[1] + (point2[1] - point3[1])

print(x, y)
