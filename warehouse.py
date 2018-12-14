import operator 

def sort_equal_quantities_alphabetically(warehouse):
    warehouse = sorted(warehouse.items(), key = operator.itemgetter(1), reverse = True)
    start = 0
    count = 1
    quantity = warehouse[0][1]
    for i in range(1, len(warehouse)):
        if quantity == warehouse[i][1]:
            count += 1
        else:
            if count > 1:
                warehouse[start:i] = sorted(warehouse[start:i], key = operator.itemgetter(0))
            start = i
            count = 1
            quantity = warehouse[i][1]
    if count > 1:
        warehouse[start:] = sorted(warehouse[start:], key = operator.itemgetter(0))
    return warehouse

T = int(input())

for _ in range(T):
    N = int(input())
    warehouse = {}
    for __ in range(N):
        shipment = input().split()
        toy = shipment[0]
        quantity = int(shipment[1])
        if toy not in warehouse:
            warehouse[toy] = 0
        warehouse[toy] += quantity
    toys = sort_equal_quantities_alphabetically(warehouse)
    print(len(toys))
    for toy in toys:
        print('%s %d' %(toy[0], toy[1]))
