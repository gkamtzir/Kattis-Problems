import sys

def calculate_flies(subwindow):
    length = len(subwindow[0])
    flies = 0
    for i in range(1, length-1):
        for j in range(1, length-1):
            if subwindow[i][j] == '*':
                flies += 1
    return flies

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')
R = int(line[0])
S = int(line[1])
K = int(line[2])

window = []

for i in range(R):
    line = sys.stdin.readline()
    line = list(line[:len(line) - 1])
    window.append(line)

max_flies = 0
coords = [-1, -1]

for i in range(S):
    if i + K > R:
        break
    for j in range(R):
        if j + K > S:
            break
        subwindow = [window[x][j:j+K] for x in range(i, i + K)]
        current_flies = calculate_flies(subwindow)
        if current_flies > max_flies:
            max_flies = current_flies
            coords[0] = i
            coords[1] = j

print(max_flies)

window[coords[0]][coords[1]] = '+'
window[coords[0]][coords[1] + K - 1] = '+'
window[coords[0] + K - 1][coords[1]] = '+'
window[coords[0] + K - 1][coords[1] + K - 1] = '+'

for j in range(coords[1] + 1, coords[1] + K - 1):
    window[coords[0]][j] = '-'

for j in range(coords[1] + 1, coords[1] + K - 1):
    window[coords[0] + K - 1][j] = '-'

for i in range(coords[0] + 1, coords[0] + K - 1):
    window[i][coords[1]] = '|'
    
for i in range(coords[0] + 1, coords[0] + K - 1):
    window[i][coords[1] + K - 1] = '|'

for row in window:
    print(''.join(row))
