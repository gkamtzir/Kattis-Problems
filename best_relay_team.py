import functools

# Custom compare function.
def compare(a, b):
    if a.get("first") < b.get("first"):
        return -1
    elif a.get("first") > b.get("first"):
        return 1
    else:
        return 0
    
def compare_other(a, b):
    if a.get("other") < b.get("other"):
        return -1
    elif a.get("other") > b.get("other"):
        return 1
    else:
        return 0

n = int(input())

runners = []

for i in range(n):
    name, first, other = map(str, input().split())
    runners.append({
        "name": name,
        "first": float(first),
        "other": float(other)
        })

# Sort by first and by other legs.
sorted_by_first = sorted(runners, key=functools.cmp_to_key(compare))
sorted_by_other = sorted(runners, key=functools.cmp_to_key(compare_other)) 

final_list = []
minimum = 200

# Find best team.
for runner in sorted_by_first:
    current_time = runner["first"]
    names = [runner["name"]]
    for other_runner in sorted_by_other:
        if other_runner["name"] != runner["name"]:
            names.append(other_runner["name"])
            current_time += other_runner["other"]
        if len(names) == 4:
            break
    if minimum > current_time:
        final_list = names[:]
        minimum = current_time

# Print results.
print(f"{minimum:.9f}")
for runner in final_list:
    print(runner)
