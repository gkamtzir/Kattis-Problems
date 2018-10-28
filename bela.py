import sys

mapper = {
    'A': {
        'dom': 11,
        'not_dom': 11
        },
    'K': {
        'dom': 4,
        'not_dom': 4
        },
    'Q': {
        'dom': 3,
        'not_dom': 3
        },
    'J': {
        'dom': 20,
        'not_dom': 2
        },
    'T': {
        'dom': 10,
        'not_dom': 10
        },
    '9': {
        'dom': 14,
        'not_dom': 0
        },
    '8': {
        'dom': 0,
        'not_dom': 0
        },
    '7': {
        'dom': 0,
        'not_dom': 0
        }
    }

line = sys.stdin.readline()
line = line[:len(line) - 1].split(' ')

hands = int(line[0])
dominant = line[1]

score = 0

for i in range(4 * hands):
    card = sys.stdin.readline()
    card = card[:len(card) - 1]
    if card[1] == dominant:
        score += mapper[card[0]]['dom']
    else:
        score += mapper[card[0]]['not_dom']

print(score)
    
