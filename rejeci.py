
def calculate_a_b(k):
    if k == 0:
        return 1, 0
    elif k == 1:
        return 0, 1
    else:
        data = [
            [1, 0],
            [0, 1]
        ]
        for _ in range(2, k + 1):
            next_pair = [data[0][0] + data[1][0], data[0][1] + data[1][1]]
            data = [data[1], next_pair]

        return data[1][0], data[1][1]
    
k = int(input())

A, B = calculate_a_b(k)
print(A, B)

