import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

numbers = []

for str_number in line:
    numbers.append(int(str_number))

numbers = sorted(numbers)

print(numbers[0]* numbers[2])


