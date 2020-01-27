P = int(input())

for i in range(P):
    data = list(map(int, input().split()))
    K = data.pop(0)
    order = []
    count = 0
    for height in data:
        inserted = False
        for index in range(len(order)):
            if order[index] > height:
                order.insert(index, height)
                count += len(order) - (index + 1)
                inserted = True
                break
        if not inserted:
            order.append(height)
    print(f"{K} {count}")
