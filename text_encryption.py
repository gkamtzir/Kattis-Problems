def encrypt(string, N):
    encrypted = [None] * len(string)
    i = 0
    initial = 0
    for letter in string:
        encrypted[i] = letter
        if i + N >= len(string):
            if initial + 1 >= len(encrypted):
                break
            if encrypted[initial + 1] is None:
                initial = initial + 1
                i = initial
                continue
            else:
                break
        i = (i + N) % len(string)
    return "".join(encrypted)

N = int(input())

while N != 0:
    string = input()
    string = string.replace(" ", "").upper()
    print(encrypt(string, N))

    N = int(input())
