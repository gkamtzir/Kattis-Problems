import math, sys

line = sys.stdin.readline()

memory = {
    }

n = 0
m = 1

while line:
    line = line[:len(line) - 1]

    for letter in line:
        if letter not in memory:
            memory[letter] = 1
        else:
            memory[letter] += 1

    for key in memory:
        n += memory[key]
        m *= math.factorial(memory[key])

    print(int(math.factorial(n)//m))

    memory = {}
    n = 0
    m = 1
    line = sys.stdin.readline()
