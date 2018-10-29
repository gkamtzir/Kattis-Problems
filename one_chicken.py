import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

N = int(line[0])
M = int(line[1])

if M >= N:
    print('Dr. Chaz will have %d piece%s of chicken left over!' % (M-N, 's' if M-N > 1 else ''))
else:
    print('Dr. Chaz needs %d more piece%s of chicken!' % (N-M, 's' if N-M > 1 else ''))
