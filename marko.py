import re

keyboard = {
    '2': '[abc]{1}',
    '3': '[def]{1}',
    '4': '[ghi]{1}',
    '5': '[jkl]{1}',
    '6': '[mno]{1}',
    '7': '[pqrs]{1}',
    '8': '[tuv]{1}',
    '9': '[wxyz]{1}'
}

N = int(input())

dictionary = []

for i in range(N):
    dictionary.append(input())

type_sequence = input()
expression = '^'

for letter in type_sequence:
    expression += keyboard[letter]

matches = 0

for word in dictionary:
    if re.match(expression, word) != None:
        matches += 1

print(matches)
