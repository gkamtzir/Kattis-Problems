import math, sys

mapper = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    '_': 26,
    '.': 27
    }

outputs = []

while(True):  
    line = sys.stdin.readline()
    line = line[:len(line)-1].split(' ')

    if line[0] == '0':
        break

    rotation = int(line[0])
    string = line[1]

    string = string[::-1]
    string = list(string)

    for index in range(len(string)):
        new_letter_index = (mapper[string[index]] + rotation) % 28
        
        for key in mapper:
            if mapper[key] == new_letter_index:
                string[index] = key
                break

    outputs.append(''.join(string))

for output in outputs:
    print(output)

