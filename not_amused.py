import sys

# Calculates each customers receipt.
def calculate(durations, day):
    price_per_minute = 0.1
    print(f"Day {day}")
    for key in sorted(durations):
        print(f"{key} ${(sum(durations[key]) * price_per_minute):.2f}")
    print("")

day = 0

for line in sys.stdin:
    line = line[:len(line) - 1]
    if line == "OPEN":
        day += 1
        checkins = {}
        durations = {}
    elif line == "CLOSE":
        calculate(durations, day)
    else:
        action, name, timestamp = map(str, line.split())
        if action == "ENTER":
            checkins[name] = int(timestamp)
            if durations.get(name) is None:
                durations[name] = []
        elif action == "EXIT":
            duration = int(timestamp) - checkins[name]
            durations[name].append(duration)
