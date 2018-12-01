n = int(input())

for i in range(n):
    s, d = map(int, input().split())
    x = (s+d) / 2
    y = x - d
    if y < 0 or (not (y).is_integer()) or (not (x).is_integer()):
        print('impossible')
    else:
        if x > y:
            print('%d %d' % (x, y))
        else:
            print('%d %d' % (y, x))
    
