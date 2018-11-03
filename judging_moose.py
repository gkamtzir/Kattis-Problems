import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
l = int(line[0])
r = int(line[1])

if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print('Even %d' % (l + r))
else:
    print('Odd %d' % (2 * r if r > l else 2 * l))
