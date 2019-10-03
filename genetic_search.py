def KMPSearch(pattern, text): 
    pattern_length = len(pattern) 
    text_length = len(text) 
  
    j = 0

    counter = 0
  
    lps = computeLPS(pattern, pattern_length) 
  
    i = 0
    while i < text_length: 
        if pattern[j] == text[i]: 
            i += 1
            j += 1
        if j == pattern_length: 
            counter += 1
            j = lps[j-1] 
        elif i < text_length and pattern[j] != text[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    return counter
  
def computeLPS(pattern, pattern_length): 
    length = 0

    lps = [0] * pattern_length
    
    i = 1
  
    while i < pattern_length: 
        if pattern[i] == pattern[length]: 
            length += 1
            lps[i] = length
            i += 1
        else: 
            if length != 0: 
                length = lps[length - 1] 
            else: 
                lps[i] = 0
                i += 1
    return lps

data = input()

while data[0] != "0":
    S, L = map(str, data.split())

    characters = ["A", "G", "C", "T"]

    type_2 = []
    type_3 = []

    type_1_counter = KMPSearch(S, L)
    type_2_counter = 0
    type_3_counter = 0

    for i in range(len(S)):
        string = S[:i] + S[i + 1:]
        if string not in type_2:
            type_2.append(string)
            type_2_counter += KMPSearch(string, L)

    for i in range(len(S)+1):
        for char in characters:
            string = S[:i] + char + S[i:]
            if string not in type_3:
                type_3.append(string)
                type_3_counter += KMPSearch(string, L)

    print(type_1_counter, type_2_counter, type_3_counter)

    data = input()
