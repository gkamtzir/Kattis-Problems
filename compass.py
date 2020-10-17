start = int(input())
end = int(input())

route_1 = end - start
route_2 = (360 - abs(route_1))

if route_1 > 0:
    route_2 = (-1) * route_2

if abs(route_1) == abs(route_2):
    print(abs(route_1))
elif abs(route_1) < abs(route_2):
    print(route_1)
else:
    print(route_2)
