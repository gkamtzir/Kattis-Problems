import sys

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

#Read input numbers
test_cases = int(sys.stdin.readline())
lines = []

for test_case in range(test_cases):
    line = sys.stdin.readline()
    line = line[:len(line)-1].split(' ')
    lines.append(line)

for line in lines:
    number_of_people = line[0]
    grades = line[1:]
    for i in range(len(grades)):
        grades[i] = int(grades[i])
    average_grade = mean(grades)
    above_average = 0
    for grade in grades:
        if grade > average_grade:
            above_average += 1
    print('{0:.3f}%'.format(above_average * 100/len(grades)))
    
