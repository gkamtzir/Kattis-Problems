import math

r, h, s = map(int, input().split())
while r != 0 or h != 0 or s != 0:
    lines = 2 * math.sqrt(h ** 2 - r ** 2)
    small_arcs = 2 * r * ((math.pi / 2) - math.acos(r/h))
    big_arc = math.pi * r
    distance = lines + small_arcs + big_arc
    distance += distance * (s/100)
    print('%.2f' % distance)
    r, h, s = map(int, input().split())

    
