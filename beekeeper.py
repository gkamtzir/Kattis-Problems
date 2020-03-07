def calculate_doubles(string):
    vowels = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True,
        "y": True
        }
    counter = 0
    for i in range(len(string) - 1):
        if vowels.get(string[i]) is not None:
            if string[i + 1] == string[i]:
                counter += 1
    return counter

N = int(input())

while N != 0:
    maximum = {
        "word": None,
        "number": -1
        }
    for i in range(N):
        string = input()
        value = calculate_doubles(string)
        if value > maximum["number"]:
            maximum["number"] = value
            maximum["word"] = string
    print(maximum["word"])
    N = int(input())
