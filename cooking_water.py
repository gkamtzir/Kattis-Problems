def who_is_right(spans, min_span):
    for span in spans:
        if span[0] < min_span[0] and span[1] < min_span[0]:
            return 'edward is right'
        if span[0] > min_span[1] and span[1] > min_span[1]:
            return 'edward is right'
    return 'gunilla has a point'

N = int(input())

min_span = []
spans = []

for _ in range(N):
    a, b = map(int, input().split())
    spans.append([a, b])
    if len(min_span) == 0:
        min_span.append(a)
        min_span.append(b)
    else:
        if min_span[1] - min_span[0] > b - a:
            min_span[0] = a
            min_span[1] = b

print(who_is_right(spans, min_span))