test_cases = int(input())

for i in range(test_cases):
    n, m = map(int, input().split())
    prizes = []
    total_cost = 0
    for j in range(n):
        data = list(map(int, input().split()))
        prizes.append(data)
    stickers = list(map(int, input().split()))
    for prize in prizes:
        done = False
        cost = prize[len(prize) - 1]
        while not done:
            indexes = []
            for j in range(1, len(prize) - 1):
                if stickers[prize[j] - 1] != 0:
                    indexes.append(prize[j] - 1)
                else:
                    done = True
                    break
            if not done:
                for index in indexes:
                    stickers[index] -= 1
                total_cost += cost
    print(total_cost)
