import math

def calculate_distance(hive1, hive2):
    return math.sqrt((hive1['coords'][0] - hive2['coords'][0])**2 + (hive1['coords'][1] - hive2['coords'][1])**2)

while True:
    data = input().split()
    d = float(data[0])
    N = int(data[1])

    hives = []
    sour = 0
    
    if N == 0 and math.isclose(d, 0.0, rel_tol=0.00):
        break

    for i in range(N):
        x, y = map(float, input().split())
        hives.append({
            'coords': [x, y],
            'sour': False
            })

    for i in range(N):
        for j in range(i + 1, N):
            distance = calculate_distance(hives[i], hives[j])
            if distance <= d:
                if not hives[i]['sour']:
                    hives[i]['sour'] = True
                    sour += 1
                if not hives[j]['sour']:
                    hives[j]['sour'] = True
                    sour += 1

    print('%d sour, %d sweet' %(sour, N - sour))
    
