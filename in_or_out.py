import sys, math

def absolute_complex(x, y):
    return math.sqrt(x**2 + y**2)

def calculate_square_complex(x, y):
    x_new = x**2 - y**2
    y_new = 2 * x * y
    return x_new, y_new

case = 0

line = sys.stdin.readline()

while line:
    line = line[:len(line) - 1].split(' ')
    case += 1
    c_x = float(line[0])
    c_y = float(line[1])
    r = int(line[2])

    z_x = 0
    z_y = 0

    done = False

    for i in range(r):

        z_x, z_y = calculate_square_complex(z_x, z_y)
        
        z_x = z_x + c_x
        z_y = z_y + c_y
        
        if absolute_complex(z_x, z_y) > 2:
            print('Case ' + str(case) + ': OUT')
            done = True
            break

    if not done:
        print('Case ' + str(case) + ': IN')

    line = sys.stdin.readline()
    
