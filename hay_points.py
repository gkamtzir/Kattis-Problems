m, n = map(int, input().split())

dictionary = {}

for i in range(m):
    word, value = map(str, input().split())
    dictionary[word] = value

for i in range(n):
    line = input()

    salary = 0

    while line != ".":
        words = line.split()
        for word in words:
            if dictionary.get(word) is not None:
                salary += int(dictionary.get(word))
        line = input()

    print(salary)
