import heapq

n, m = map(int, input().split())

tasks_slots = list(map(int, input().split()))
heapq.heapify(tasks_slots)

quiet_slots = list(map(int, input().split()))
heapq.heapify(quiet_slots)

counter = 0

while n > 0:
    task_slot = heapq.heappop(tasks_slots)
    n -= 1
    while True:
        quiet_slot = heapq.heappop(quiet_slots)
        m -= 1
        if task_slot <= quiet_slot:
            counter += 1
            break
        if m == 0:
            break
    if m == 0:
        break  

print(counter)
