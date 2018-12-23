import sys

line = sys.stdin.readline()
used_words = []

while line:
    text = line
    text = text[:len(text) - 1]
    text = text.split(' ')
    for word in text:
        word = word.lower()
        if word in used_words:
            print('.', end = ' ')
        else:
            used_words.append(word)
            print(word, end = ' ')
    line = sys.stdin.readline()
