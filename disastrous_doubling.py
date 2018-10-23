import sys

garbage = int(sys.stdin.readline())

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
b_vector = [int(x) for x in line]

error = False
bacteria_left = 1

for b in b_vector:
    bacteria_left = bacteria_left * 2
    if b <= bacteria_left:
        bacteria_left -= b
    else:
        print('error')
        error = True
        break

if not error:
    print(bacteria_left % (10**9 + 7))
