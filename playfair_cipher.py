import sys

def populate_table(key_phrase, alpabet):
    table = []
    for letter in key_phrase:
        if letter.upper() not in table and letter.upper() != ' ':
            table.append(letter.upper())
    for letter in alphabet:
        if letter.upper() not in table:
            table.append(letter.upper())
    return table

def index_to_ij(index):
    row = index // 5
    col = index % 5
    return row, col

key_phrase = sys.stdin.readline()
key_phrase = key_phrase[:len(key_phrase) - 1]

text = sys.stdin.readline()
text = text[:len(text) - 1]

#Alphabet without 'Q'
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']

table = populate_table(key_phrase, alphabet)

text = [x.upper() for x in text if x != ' ']

i = 0

while i < len(text):
    if i + 1 >= len(text):
        text.append('X')
    if text[i] == text[i+1]:
        text.insert(i+1, 'X')
    
    first = table.index(text[i])
    second = table.index(text[i+1])
    row_1, col_1 = index_to_ij(first)
    row_2, col_2 = index_to_ij(second)

    if row_1 == row_2:
        text[i] = table[5 * row_1 + (col_1 + 1) % 5]
        text[i + 1] = table[5 * row_2 + (col_2 + 1) % 5]
    elif col_1 == col_2:
        text[i] = table[5 * ((row_1 + 1) % 5) + col_1]
        text[i+1] = table[5 * ((row_2 + 1) % 5) + col_2]
    else:
        text[i] = table[5 * row_1 + col_2]
        text[i+1] = table[5 * row_2 + col_1]

    i += 2

print(''.join(text))

