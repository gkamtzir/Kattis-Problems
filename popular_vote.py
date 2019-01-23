T = int(input())

for _ in range(T):
    n = int(input())
    votes = []
    for i in range(n):
        vote = int(input())
        votes.append(vote)
    max_vote = max(votes)
    winner_id = votes.index(max_vote)
    votes = sorted(votes, reverse=True)
    if votes[0] == votes[1]:
        print("no winner")
    else:
        total_votes = sum(votes)
        if max_vote > int(total_votes/2):
            print("majority winner %d" % (winner_id + 1))
        else:
            print("minority winner %d" % (winner_id + 1))
