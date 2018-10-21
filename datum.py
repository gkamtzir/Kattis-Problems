import sys

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_index = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']


day = int(line[0])
month = int(line[1])

count = 0

for i in range(month - 1):
    count += month_days[i]

count += day
print(day_index[count % 7])
