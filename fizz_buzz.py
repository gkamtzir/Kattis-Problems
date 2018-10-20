import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

x = int(line[0])
y = int(line[1])
n = int(line[2])

for i in range(1, n+1):
    if i % x == 0 and i % y == 0:
        print('FizzBuzz')
    elif i % x == 0:
        print('Fizz')
    elif i % y == 0:
        print('Buzz')
    else:
        print(i)
