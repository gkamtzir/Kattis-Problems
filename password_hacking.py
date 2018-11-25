N = int(input())

probs = []

for i in range(N):
    line = input().split()
    password = line[0]
    prob = float(line[1])
    probs.append(prob)

probs = sorted(probs, reverse = True)

result = 0

for i in range(len(probs)):
    result += probs[i] * (i + 1)

print(result)
