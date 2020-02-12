n, p, k = map(int, input().split())

t = list(map(int, input().split()))

result = 0
seconds_sum = 0
previous = 0
factor = 1

for timestamp in t:
    print(previous)
    print(timestamp)
    seconds = timestamp - previous
    seconds_sum += seconds
    result += seconds * factor

    # Updating variables
    previous = timestamp
    factor += p / 100

result += (k - seconds_sum) * factor

print(f"{result:.6f}")
