n = int(input())

candidates = {}

for i in range(n):
    candidate = input()
    party = input()
    candidates[candidate] = party

m = int(input())

votes = {}

for i in range(m):
    candidate = input()
    if candidates.get(candidate) is None:
        continue
    if votes.get(candidate) is not None:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

max_votes = -1
winning_candidate = None
tie = False

for key, value in votes.items():
    if value > max_votes:
        max_votes = value
        winning_candidate = key
        tie = False
    elif value == max_votes:
        tie = True

if not tie and winning_candidate is not None:
    print(candidates.get(winning_candidate))
else:
    print("tie")
