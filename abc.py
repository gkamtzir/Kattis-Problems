import sys

mapper = {
    'A': 0,
    'B': 1,
    'C': 2
    }

#Read input numbers
line = sys.stdin.readline()

input_numbers = []

for number in line[:len(line)-1].split(' '):
    input_numbers.append(int(number))

#Read input letters
line = sys.stdin.readline()

input_letters = []
line = line[:len(line)-1].split(' ')[0]

for letter in line:
    input_letters.append(letter)

input_numbers = sorted(input_numbers)

for i in input_letters:
    print(input_numbers[mapper[i]], end=' ')
