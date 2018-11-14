import sys

def rotate_grille(grille, n):
    new_grille = []
    for i in range(n):
        new_grille.append([])
            
    for i in range(n):
        for j in range(n):
            new_grille[j].insert(0, grille[i][j])

    return new_grille

def decrypt(message, grille, n):
    decrypted_message = []
    for i in range(n):
        decrypted_message.append([])
        for j in range(n):
            decrypted_message[i].append('.')
    for k in range(4):
        for i in range(n):
            for j in range(n):
                if grille[i][j] == '.':
                    if decrypted_message[i][j] != '.':
                        return 'invalid grille'
                    decrypted_message[i][j] = message.pop(0)  
        grille = rotate_grille(grille, n)
    
    final_message = ''
    for i in range(n):
        for j in range(n):
            if decrypted_message[i][j] == '.':
                return 'invalid grille'
            final_message += decrypted_message[i][j]
    return final_message

    

n = int(sys.stdin.readline())

grille = []

for i in range(n):
    line = sys.stdin.readline()
    line = list(line[:len(line) - 1])
    grille.append(line)

message = sys.stdin.readline()
message = message[:len(message) - 1]

print(decrypt(list(message), grille, n))
