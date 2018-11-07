import math, sys

def encode(data):
    encoded = ''
    current_letter = ''
    count = 0
    for letter in data:
        if letter != current_letter:
            if current_letter != '':
                encoded += (current_letter + str(count))
            current_letter = letter
            count = 1
            continue
        count += 1
    encoded += (current_letter + str(count))
    return encoded

def decode(data):
    decoded = ''
    for index in range(0, len(data), 2):
        occurences = int(data[index + 1])
        decoded += (data[index] * occurences)
    return decoded

line = sys.stdin.readline()
line = line[:len(line)-1].split(' ')

mode = line[0]
data = line[1]

if mode == 'E':
    print(encode(data))
else:
    print(decode(data))

