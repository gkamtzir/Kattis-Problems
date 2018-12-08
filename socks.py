S, C, K = map(int, input().split())

colors = list(map(int, input().split()))

colors = sorted(colors)

if C >= S:
    washing_machines = 1
else:
    washing_machines = 0
    lower = 0
    while True:
        if lower >= S:
            break
        upper = lower + C - 1
        if upper >= S:
            upper = S - 1
        while upper >= lower:
            if colors[upper] - colors[lower] <= K:
                washing_machines += 1
                lower = upper + 1
                break
            upper -= 1
        
print(washing_machines)
