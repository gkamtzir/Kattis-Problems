n = int(input())

for i in range(n):
    data = input().split()
    m = int(data[0])
    result1 = 0
    result2 = 0
    for j in range(1, 2 * m - 2, 2):
        result1 += int(data[j]) * int(data[j + 3])
    result1 += int(data[2 * m - 1]) * int(data[2])
    for j in range(2, 2 * m - 1, 2):
        result2 += int(data[j]) * int(data[j + 1])
    result2 += int(data[2 * m]) * int(data[1])
    print((result1 - result2) / 2)
