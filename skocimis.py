import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
A = int(line[0])
B = int(line[1])
C = int(line[2])

moves = 0

while B - A > 1 or C - B > 1:
    span_AB = B - A
    span_BC = C - B
    if span_AB > span_BC:
        C = B
        B = A + 1
        moves += 1
    else:
        A = B
        B = C - 1
        moves += 1

print(moves)
        
