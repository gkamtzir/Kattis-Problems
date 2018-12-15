import re

def check_if_rhymes(last_word, endings):
    for end in endings:
        indices = [m.start() for m in re.finditer('(?=' + end + ')', last_word)]
        if len(indices) > 0:
            last_occurrence = indices.pop()
            if last_occurrence + len(end) == len(last_word):
                return 'YES'
    return 'NO'

word = input()
E = int(input())
endings = []
for _ in range(E):
    candidate_endings = input().split()
    if check_if_rhymes(word, candidate_endings) == 'YES':
        for end in candidate_endings:
            if end not in endings:
                endings.append(end)
P = int(input())
for _ in range(P):
    sentence = input().split()
    last_word = sentence.pop()
    print(check_if_rhymes(last_word, endings))
