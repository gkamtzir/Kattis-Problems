import functools

# Custom compare function.
def compare(a, b):
    if a.get("data") > b.get("data"):
        return -1
    elif a.get("data") < b.get("data"):
        return 1
    else:
        if a.get("index") < b.get("index"):
            return -1
        else:
            return 1

N, C = map(int, input().split())

data = {}

numbers = list(map(int, input().split()))

# Storing data.
for i in range(len(numbers)):
    if data.get(str(numbers[i])) is None:
        data[str(numbers[i])] = {}
        data[str(numbers[i])]["index"] = i
        data[str(numbers[i])]["value"] = numbers[i]
        data[str(numbers[i])]["data"] = 1
    else:
        data[str(numbers[i])]["data"] += 1

list_data = [data.get(item) for item in data]

# Sorting data
list_data = sorted(list_data, key=functools.cmp_to_key(compare))

# Displaying data.
for item in list_data:
    for i in range(item["data"]):
        print(item["value"], end=" ")

