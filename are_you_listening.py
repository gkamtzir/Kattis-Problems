import math

def get_detected_devices(cx, cy, radius, devices):
    detected = 0
    for device in devices:
        distance = math.sqrt((cx - device[0]) ** 2 + (cy - device[1]) ** 2)
        if distance < radius + device[2]:
            detected += 1
            if detected == 3:
                break
    return detected

# Reading input data.
cx, cy, n = map(int, input().split())

devices = []

for _ in range(n):
    x, y, r = map(int, input().split())
    devices.append([x, y, r])

steps = [100, 10, 1]
step_index = 0
radius = 1

while True:
    detected = get_detected_devices(cx, cy, radius, devices)
    if detected == 3:
        if radius == 1:
            radius = 0
            break
        if step_index == 2:
            radius -= steps[step_index]
            break
        else:
            radius -= steps[step_index]
            step_index += 1
            radius += steps[step_index]
    else:
        radius += steps[step_index]
print(radius)
