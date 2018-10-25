import sys

mapper = {
    'c': [2, 3, 4, 7, 8, 9, 10],
    'd': [2, 3, 4, 7, 8, 9],
    'e': [2, 3, 4, 7, 8],
    'f': [2, 3, 4, 7],
    'g': [2, 3, 4],
    'a': [2, 3],
    'b': [2],
    'C': [3],
    'D': [1, 2, 3, 4, 7, 8, 9],
    'E': [1, 2, 3, 4, 7, 8],
    'F': [1, 2, 3, 4, 7],
    'G': [1, 2, 3, 4],
    'A': [1, 2, 3],
    'B': [1, 2]
    }

test_cases = int(sys.stdin.readline())

for i in range(test_cases):
    notes = sys.stdin.readline()
    notes = notes[:len(notes) - 1]

    presses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 

    fingers_used = []
    for note in notes:
        fingers_used_new = []
        for finger in mapper[note]:
            if finger not in fingers_used:
                fingers_used_new.append(finger)
                presses[finger - 1] += 1
            else:
                fingers_used_new.append(finger)
        fingers_used = fingers_used_new[:]

    for number in presses:
        print(number, end=' ')
    print()
    
