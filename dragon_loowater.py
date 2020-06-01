def get_cost(heads, knights):
    if len(heads) > len(knights):
        return None
    position = 0
    cost = 0
    for head in heads:
        found = False
        for i in range(position, len(knights)):
            if knights[i] >= head:
                position = i + 1
                cost += knights[i]
                found = True
                break
        if not found:
            return None
    return cost

number_of_heads, number_of_knights = map(int, input().split())

while number_of_heads != 0 or number_of_knights != 0:
    heads = []
    knights = []
    for i in range(number_of_heads):
        heads.append(int(input()))
    for i in range(number_of_knights):
        knights.append(int(input()))

    heads = sorted(heads)
    knights = sorted(knights)

    cost = get_cost(heads, knights)

    if cost is None:
        print("Loowater is doomed!")
    else:
        print(cost)
        
    number_of_heads, number_of_knights = map(int, input().split())
