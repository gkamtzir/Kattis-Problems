import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

n = int(line[0])
capacity = int(line[1])

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
weights = [int(x) for x in line]

m = []

for i in range(n+1):
    m.append([])

for i in range(capacity+1):
    m[0].append(0)

for i in range(1, n+1):
    for j in range(capacity+1):
        if weights[i-1] > j:
            m[i].append(m[i - 1][j])
        else:
            m[i].append(max([m[i - 1][j], m[i - 1][j - weights[i-1]] + 1]))
            
print(m[n][capacity])
