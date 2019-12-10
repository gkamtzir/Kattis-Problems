valid = int(input())

my_answers = input()
others_answers = input()

total = len(my_answers)

matches = 0

for i in range(total):
    if my_answers[i] == others_answers[i]:
        matches += 1

print(min([valid, matches]) + total - max([valid, matches]))
