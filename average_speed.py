import sys

def subtract_timestamps(time_1, time_2):
    time_1 = time_1.split(':')
    time_2 = time_2.split(':')
    seconds_1 = int(time_1[0]) * 3600 + int(time_1[1]) * 60 + int(time_1[2])
    seconds_2 = int(time_2[0]) * 3600 + int(time_2[1]) * 60 + int(time_2[2])
    return 0.0 if seconds_1 == seconds_2 else (seconds_2 - seconds_1) / 3600

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

current_timestamp = line[0]
total_distance = 0.0

if len(line) == 1:
    speed = 0
    print('%s %.2f km' % (line[0], total_distance))
else:
    speed = int(line[1])

line = sys.stdin.readline()

while line:
    line = line[:len(line) - 1].split(' ')
    previous_timestamp = current_timestamp
    current_timestamp = line[0]
    time = subtract_timestamps(previous_timestamp, current_timestamp)
    total_distance += speed * time
    if len(line) == 1:
        #query
        print('%s %.2f km' % (line[0], total_distance))
    else:
        #speed change
        speed = int(line[1])
    line = sys.stdin.readline()
