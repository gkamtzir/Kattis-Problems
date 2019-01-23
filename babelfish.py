import sys

line = sys.stdin.readline()
line = line[:len(line) - 1]

dictionary = {}

#Populate dictionary
while line != '':
    line = line.split(' ')
    english = line[0]
    waterloo = line[1]
    if waterloo not in dictionary:
        dictionary[waterloo] = english
    line = sys.stdin.readline()
    line = line[:len(line) - 1]

line = sys.stdin.readline()

while line:
    line = line[:len(line) - 1]
    if line in dictionary:
        print(dictionary[line])
    else:
        print('eh')
    line = sys.stdin.readline()
