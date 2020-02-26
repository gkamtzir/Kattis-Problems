maximum = -1
winner = -1

for i in range(5):
    data = list(map(int, input().split()))
    result = sum(data)
    if result > maximum:
        maximum = result
        winner = i
print(f"{winner+1} {maximum}")
