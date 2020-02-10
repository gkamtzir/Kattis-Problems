N = int(input())

record = {}

for i in range(N):
    costume = input()
    if record.get(costume) is None:
        record[costume] = 1
    else:
        record[costume] += 1

minimum = N + 1
selections = []

for key, value in record.items():
    if value < minimum:
        minimum = value
        selections = [key]
    elif value == minimum:
        selections.append(key)

for costume in sorted(selections):
    print(costume)
