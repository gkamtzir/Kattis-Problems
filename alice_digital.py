import sys

number_of_datasets = int(sys.stdin.readline())

for i in range(number_of_datasets):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split(' ')
    n = int(line[0])
    m = int(line[1])
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split(' ')
    a = [int(x) for x in line]
    max_total = 0
    total = 0
    index = 0
    while True:
        if index >= n:
            break
        total = 0
        occurences = 0
        occurence_index = 0
        while index < n:
            if a[index] < m:
                if occurences == 0:
                    total = 0
                index += 1
                break
            total += a[index]
            if a[index] == m:
                occurences += 1
                if occurences == 1:
                    occurence_index = index + 1
                elif occurences == 2:
                    total -= m
                    index = occurence_index
                    break
            index += 1
        if total > max_total:
            max_total = total
    print(max_total)
