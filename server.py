n, T = map(int, input().split())

tasks = list(map(int, input().split()))

total_time = 0
tasks_counter = 0

for task in tasks:
    if total_time + task <= T:
        total_time += task
        tasks_counter += 1
    else:
        break

print(tasks_counter)
