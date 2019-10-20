import sys

for line in sys.stdin:
    line = line[:len(line) - 1]
    month, day, year, rise_time, set_time = map(str, line.split())

    # Converting time to integers.
    rise_time = list(map(int, rise_time.split(":")))
    set_time = list(map(int, set_time.split(":")))

    # Calculating the difference.
    hours = set_time[0] - rise_time[0]

    minutes = set_time[1] - rise_time[1]

    # Checking if rise time minutes are greater
    # than set time minutes.
    if minutes < 0:
        hours -= 1
        minutes = 60 + minutes
    
    print(f"{month} {day} {year} {hours} hours {minutes} minutes")
