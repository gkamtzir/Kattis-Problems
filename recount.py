import operator

vote = input()

votes = {}
total = 0

while vote != '***':
    if vote not in votes:
        votes[vote] = 0
    votes[vote] += 1
    total += 1
    vote = input()

for candidate in votes:
    votes[candidate] = votes[candidate] / total

votes = sorted(votes.items(), key = operator.itemgetter(1), reverse = True)
if abs(votes[0][1] - votes[1][1]) > 0.001:
    print(votes[0][0])
else:
    print('Runoff!')
