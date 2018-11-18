import sys

n = sys.stdin.readline()
case = 1
while n:
    n = int(n)

    numbers = []

    for i in range(n):
        numbers.append(int(sys.stdin.readline()))

    numbers = sorted(numbers)

    m = int(sys.stdin.readline())

    queries = []
    answers = []
    print('Case %d:' % case)
    for i in range(m):
        query = int(sys.stdin.readline())
        queries.append(query)
        lo_index = 0
        hi_index = len(numbers) - 1
        last_sum = ''
        while lo_index < hi_index:
            pair_sum = numbers[lo_index] + numbers[hi_index]
            if pair_sum < query:
                lo_index += 1
            elif pair_sum > query:
                hi_index -= 1
            else:
                last_sum = pair_sum
                break
            if last_sum == '':
                last_sum = pair_sum
                continue
            if abs(pair_sum - query) < abs(last_sum - query):
                    last_sum = pair_sum
        print('Closest sum to %d is %d.' % (query, last_sum))

    n = sys.stdin.readline()
    case += 1
