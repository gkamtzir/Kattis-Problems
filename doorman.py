X = int(input())

line = list(input())

count_men = 0
count_women = 0

while len(line) > 0 and abs(count_men - count_women) <= X:
    if abs(count_men - count_women) <= X:
        person = line.pop(0)
        if person == 'M':
            count_men += 1
            if abs(count_men - count_women) == X + 1:
                if len(line) > 0 and line[0] == 'W':
                    line[0] = 'M'
                    count_men -= 1
                    count_women += 1
                else:
                    count_men -= 1
                    break
        else:
            count_women += 1
            if abs(count_men - count_women) == X + 1:
                if len(line) > 0 and line[0] == 'M':
                    line[0] = 'W'
                    count_women -= 1
                    count_men += 1
                else:
                    count_women -= 1
                    break

print(count_men + count_women)
