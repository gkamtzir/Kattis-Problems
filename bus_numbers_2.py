N = int(input())

buses = list(map(int, input().split(" ")))

buses.sort()

current_span = []
answers = []

for bus in buses:
    if len(current_span) == 0:
        current_span.append(bus)
    else:
        if current_span[len(current_span) - 1] - bus == -1:
            current_span.append(bus)
        elif len(current_span) == 2:
            answers = answers + current_span
            current_span = [bus]
        elif len(current_span) == 1:
            answers.append(current_span[0])
            current_span = [bus]
        else:
            answers.append(f'{current_span[0]}-{current_span[len(current_span) - 1]}')
            current_span = [bus]

if len(current_span) == 2:
    answers = answers + current_span
elif len(current_span) > 2:
    answers.append(f'{current_span[0]}-{current_span[len(current_span) - 1]}')
elif len(current_span) == 1:
    answers.append(current_span[0])

for answer in answers:
    print(answer, end = " ")
