import functools

def compare_words(word1, word2):
    if word1["count"] < word2["count"]:
        return 1
    elif word1["count"] > word2["count"]:
        return -1
    else:
        if word1["value"] < word2["value"]:
            return -1
        elif word1["value"] > word2["value"]:
            return 1
        else:
            return 0

M = int(input())

user_log = {}

for _ in range(M):
    data = input().split()
    user = data[0]
    if user_log.get(user) is None:
        user_log[user] = {}
    for word in data[1:]:
        if user_log[user].get(word) is None:
            user_log[user][word] = 1
        else:
            user_log[user][word] += 1

same_words = []

for user_key in user_log:
    for value in user_log[user_key]:
        invalid = False
        count = 0
        for other_user_key in user_log:
            if user_log[other_user_key].get(value) is None:
                invalid = True
            else:
                count += user_log[other_user_key][value]
        if not invalid:
            same_words.append({
                "value": value,
                "count": count
                })
    break

if len(same_words) == 0:
    print("ALL CLEAR")
else:
    for item in sorted(same_words, key = functools.cmp_to_key(compare_words)):
        print(item["value"])
