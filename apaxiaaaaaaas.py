import sys

line = sys.stdin.readline()
line = line[:len(line)-1]

result = ''
temp = ''

for letter in line:
    if temp != letter:
        temp = letter
        result += temp

print(result)
