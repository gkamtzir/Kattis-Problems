C, X, M = map(float, input().split())

table = []
final_speed = None

for i in range(6):
    speed, efficiency = map(float, input().split())
    total_gas = (M / efficiency) + (M / speed) * X
    if total_gas - (C/2) <= 0.000001:
        final_speed = speed

if final_speed != None:
    print(f"Yes {int(final_speed)}")
else:
    print("No")
