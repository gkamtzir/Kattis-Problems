year = int(input())

current_year = 2018
current_month = 4

while True:
    if current_year == year:
        print("yes")
        break
    if current_year > year:
        print("no")
        break
    current_year += 2
    current_month += 2
    if current_month > 12:
        current_year += 1
        current_month = current_month - 12
