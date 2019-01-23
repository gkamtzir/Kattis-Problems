import math

def find_square(number):
    square_number = math.sqrt(number)
    if square_number == int(square_number):
        return int(square_number)
    else:
        return int(square_number) + 1

def rotate_matrix_message(matrix_message, m):
    new_message = []
    for _ in range(m):
        new_message.append([])
            
    for i in range(m):
        for j in range(m):
            new_message[j].insert(0, matrix_message[i][j])

    return new_message

def create_matrix_message(message, m):
    matrix_message = []
    for i in range(m):
        matrix_message.append([])
        for j in range(m):
            if len(message) > 0:
                matrix_message[i].append(message.pop(0))
            else:
                matrix_message[i].append('*')
    return matrix_message

def print_message(matrix_message, m):
    message = ''
    for i in range(m):
        for j in range(m):
            if matrix_message[i][j] != '*':
                message += matrix_message[i][j]
    return message

n = int(input())

for _ in range(n):
    message = list(input())
    m = find_square(len(message))
    matrix_message = create_matrix_message(message, m)
    encrypted_message = rotate_matrix_message(matrix_message, m)
    print(print_message(encrypted_message, m))
