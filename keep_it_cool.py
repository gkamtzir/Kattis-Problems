from operator import itemgetter

n, m, s, d = map(int, input().split())

slots = list(map(int, input().split()))
answer = [0] * s

new_slots = []

for i in range(len(slots)):
    new_slots.append({
        "i": i,
        "capacity": slots[i]
    })

new_slots = sorted(new_slots, key=itemgetter("capacity"))

slot = 0

while n > 0 and slot < len(new_slots):
    if d - new_slots[slot]["capacity"] <= n:
        added = d - new_slots[slot]["capacity"]
    else:
        added = n
    answer[new_slots[slot]["i"]] = added
    n -= added
    slot += 1

cold_drinks = 0

for i in range(len(answer)):
    if answer[i] == 0:
        cold_drinks += slots[i]

if cold_drinks >= m:
    answer_output = ""
    for item in answer:
        answer_output += f"{item} "
    print(answer_output.strip(), end="")
else:
    print("impossible")
