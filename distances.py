import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

while True:

    if int(float(line[0])) == float(line[0]) and int(float(line[0])) == 0:
        break
    
    x_1 = float(line[0])
    y_1 = float(line[1])

    x_2 = float(line[2])
    y_2 = float(line[3])

    p = float(line[4])

    answer = (abs(x_1 - x_2)**p + abs(y_1 - y_2)**p)**(1/p)

    print('%.10f' % answer)

    line = sys.stdin.readline()
    line = line[:len(line) - 1].split(' ')
