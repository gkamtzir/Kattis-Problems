from operator import itemgetter

def update_number_of_cars(number_of_cars, timestamp_type):
    if timestamp_type == "start":
        return number_of_cars + 1
    else:
        return number_of_cars - 1

A, B, C = map(int, input().split())

timestamps = []
costs = [A, B, C]

for i in range(3):
    start, end = map(int, input().split())
    timestamps.append({
        "type": "start",
        "value": start
        })
    timestamps.append({
        "type": "end",
        "value": end
        })

timestamps = sorted(timestamps, key = itemgetter('value'))

number_of_cars = 0
previous = -1
cost = 0

for timestamp in timestamps:
    if number_of_cars != 0:
        cost += (timestamp["value"] - previous) * costs[number_of_cars - 1] * (number_of_cars)
    previous = timestamp["value"]
    number_of_cars = update_number_of_cars(number_of_cars, timestamp["type"])

print(cost)
