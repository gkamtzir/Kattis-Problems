import sys

line = sys.stdin.readline()

words = []
while line:
    line = line[:len(line) - 1].split(' ')
    words += line
    line = sys.stdin.readline()

concat_words = []

for i in range(len(words)):
    for j in range(len(words)):
        if i == j:
            continue
        else:
            concat_words.append(words[i] + words[j])

concat_words = sorted(list(set(concat_words)))

for word in concat_words:
    print(word)
