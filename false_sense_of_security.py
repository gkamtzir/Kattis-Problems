import sys

mapper = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--',
    '.': '---.',
    ',': '.-.-',
    '?': '----'
    }

line = sys.stdin.readline()

while line:
    line = line[:len(line) - 1]

    encoded_string = ''
    decoded_string = ''
    index = []

    for letter in line:
        encoded_string += mapper[letter]
        index.append(len(mapper[letter]))

    index = index[::-1]

    pointer = 0

    for i in index:
        decoded_string += [key for key, value in mapper.items() if value == encoded_string[pointer: pointer + int(i)]][0]
        pointer += int(i)

    print(decoded_string)
    line = sys.stdin.readline()
