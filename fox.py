N = int(input())

for _ in range(N):
    voices = input().split()
    distinct_info = []
    info = input()
    while info != 'what does the fox say?':
        info = info.split()
        if info[2] not in distinct_info:
            distinct_info.append(info[2])
        info = input()
    for voice in voices:
        if voice not in distinct_info:
            print(voice, end = ' ')
