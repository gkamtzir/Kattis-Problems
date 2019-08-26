n = int(input())

items = list(map(int, input().split()))
candidates = []
max_item = None

for item in items:
    # Check if it's a candidate.
    if max_item == None or max_item < item:
        max_item = item
        candidates.append(item)
    else:
        # Check if it affects any other candidate.
        while True:
            if len(candidates) == 0:
                break
            if candidates[len(candidates) - 1] < item:
                break
            candidates.pop()

print(len(candidates))
