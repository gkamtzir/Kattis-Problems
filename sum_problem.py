import sys

data_sets = int(sys.stdin.readline())

memory = {
    'positive': {
        'total': 0,
        'count': 0
        },
    'even': {
        'total': 0,
        'count': 0
        },
    'odd': {
        'total': 0,
        'count': 0
        }
    }

for i in range(data_sets):
    line = sys.stdin.readline()
    line = line[:len(line) - 1].split(' ')
    line = [int(x) for x in line]

    K = line[0]
    N = line[1]

    positive = N * (2 + (N-1) * 1)/2
    odd = N * (2 + (N-1) * 2)/2
    even = N * (4 + (N-1) * 2)/2
    
    print('%d %d %d %d' % (K, positive, odd, even))
