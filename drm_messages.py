def rotate(string):
    new_string = ""
    value = 0
    for letter in string:
        value += ord(letter) - 65
    for letter in string:
        number = 65 + ((ord(letter) - 65 + value) % 26)
        new_string += chr(number)
    return new_string

def merge(first_half, second_half):
    new_string = ""
    for i in range(len(first_half)):
        value = ord(second_half[i]) - 65
        value = 65 + ((value + ord(first_half[i]) - 65) % 26)
        new_string += chr(value)
    return new_string

string = input()

first_half = string[:len(string)//2]
second_half = string[len(string)//2:]

print(merge(rotate(first_half), rotate(second_half)))


