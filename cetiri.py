def find_missing_value(data, difference):
    for i in range(len(data) - 1):
        if data[i+1] != difference + data[i]:
            return difference + data[i]
    return data[len(data) - 1] + difference

data = input().split()
data = [int(x) for x in data]

data = sorted(data)
difference = -1

for i in range(len(data) - 1):
    current_difference = data[i+1] - data[i]
    if difference == -1 or difference > current_difference:
        difference = current_difference

print(find_missing_value(data, difference))
