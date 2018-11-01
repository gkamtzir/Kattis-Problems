import sys

number_of_books = int(sys.stdin.readline())

book_costs = []

for i in range(number_of_books):
    book = int(sys.stdin.readline())
    book_costs.append(book)

book_costs = sorted(book_costs, reverse = True)

cost = 0
index = 1

for price in book_costs:
    if index % 3 == 0:
        index += 1
        continue
    cost += price
    index += 1

print(cost)
