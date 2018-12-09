import sys

data = sys.stdin.readline()
case = 1

while data:
    data = data[:len(data) - 1].split()
    data = [int(x) for x in data]
    earth_days = data[0]
    mars_days = data[1]
    count = 0
    while not (earth_days == mars_days and earth_days == 0):
        earth_days = (earth_days + 1) % 365
        mars_days = (mars_days + 1) % 687
        count += 1
    print('Case %d: %d' %(case, count))
    case += 1
    data = sys.stdin.readline()
