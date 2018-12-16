def find_nearest(letter, search):
    distance = 1000
    match = ''
    for alphabet_letter in search:
        if abs(ord(letter) - ord(alphabet_letter)) < distance and letter != alphabet_letter:
            distance = abs(ord(letter) - ord(alphabet_letter))
            match = alphabet_letter
    return match

endings = ['a', 'o', 'u']
consonants = ['b', 'c', 'd', 'g', 'k', 'n', 'p', 't']
sentence = input().split()

translated = ''
for word in sentence:
    word = list(word)
    first_syllabus = True
    for i in range(len(word)):
        upper = False
        if i == 0:
            #Check if letter is uppercase.
            if ord(word[i]) < 97:
                upper = True
            word[i] = word[i].lower()
            if word[i] not in consonants:
                word[i] = find_nearest(word[i], consonants)
            if upper:
                word[i] = word[i].upper()
        else:
            if word[i] == '-':
                first_syllabus = False
            if word[i] in consonants and not first_syllabus:
                word[i] = word[0].lower()
    if word[len(word) - 1].lower() in consonants:
        word += [find_nearest(word[len(word) - 1].lower(), endings) + 'h']
    word = [letter for letter in word if letter != '-']
    print(''.join(word), end = ' ')
