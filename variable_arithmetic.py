memory = {}

line = input()

while line != "0":
    line = line.split()

    if len(line) > 1 and line[1] == "=":
        memory[line[0]] = int(line[2])
    else:
        numeric = 0
        result = ""
        for i in range(0, len(line), 2):
            try:
                numeric += int(line[i])
            except ValueError:
                if memory.get(line[i]) is not None:
                    numeric += memory[line[i]]
                else:
                    if result != "":
                        result += f" + {line[i]}"
                    else:
                        result += line[i]
        if result != "":
            print(f"{str(numeric) + ' + ' if numeric > 0 else ''}{result}")
        else:
            print(numeric)
    
    line = input()
