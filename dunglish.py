n = int(input())

groups = {}
correct = {}
total = {}
temp = {}

sentence = input().split()

for item in sentence:
    if groups.get(item) is None:
        groups[item] = 1
    else:
        groups[item] += 1

m = int(input())

for i in range(m):
    data = input().split()
    if data[2] == "correct":
        if correct.get(data[0]) is None:
            correct[data[0]] = 1
        else:
            correct[data[0]] += 1
            
    if total.get(data[0]) is None:
        total[data[0]] = 1
    else:
        total[data[0]] += 1

    temp[data[0]] = data[1]

total_correct = 1
total_total = 1

for key, value in groups.items():
    if correct.get(key) is not None:
        total_correct *= correct[key] ** value
    else:
        total_correct = 0
    total_total *= total[key] ** value

if total_total == 1 and total_correct == 1:
    for item in sentence:
        print(temp[item], end=" ")
    print("\ncorrect")
elif total_total == 1:
    for item in sentence:
        print(temp[item], end=" ")
    print("\nincorrect")
else:
    print(f"{total_correct} correct")
    print(f"{total_total - total_correct} incorrect")

