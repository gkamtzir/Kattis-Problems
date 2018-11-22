test_cases = int(input())

for i in range(test_cases):
    D, M = map(int, input().split())

    days_in_month = input().split()
    days_in_month = [int(x) for x in days_in_month]

    count = 0
    start_day = 0
    friday = 5

    for days in days_in_month:
        if days >= 13:
            day_13 = (start_day + 12) % 7
            if day_13 == friday:
                count += 1
        start_day = (start_day + days) % 7

    print(count)
