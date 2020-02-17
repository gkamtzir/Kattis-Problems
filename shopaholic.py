n = int(input())

items = sorted(list(map(int, input().split())), reverse=True)

discount = 0

for i in range(0, len(items), 3):
    if i + 1 >= len(items) or i + 2 >= len(items):
        break
    discount += items[i + 2]

print(discount)
