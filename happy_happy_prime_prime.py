def is_prime(number):
    i = 2
    if number <= 1:
        return False
    while True:
        if number / 2 <= i:
            return True
        elif number % i == 0:
            return False
        i += 1

P = int(input())

for i in range(P):
    K, m = map(int, input().split())
    if not is_prime(m):
        print(f"{i+1} {m} NO")
        continue
    total_sum = str(m)
    total = 0
    iteration = 0
    while iteration < 1000:
        for str_number in total_sum:
            number = int(str_number)
            total += number ** 2
        if total == 1:
            print(f"{i+1} {m} YES")
            break
        total_sum = str(total)
        total = 0
        iteration += 1
    if iteration == 1000:
        print(f"{i+1} {m} NO")
