N = int(input())

cups = {}

for i in range(N):
    data = input().split()
    try:
        radius = int(data[0])
        label = data[1]
        radius = radius / 2
    except ValueError:
        radius = int(data[1])
        label = data[0]
    cups[radius] = label

for key in sorted(cups):
    print(cups[key])

