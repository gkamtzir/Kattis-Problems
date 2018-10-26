import sys

line = sys.stdin.readline()

memory = {

    }

while line:
    line = line[:len(line) - 1].split(' ')
    if line[0] == 'def':
        variable = line[1]
        value = int(line[2])
        memory[variable] = value
    elif line[0] == 'calc':
        error = False
        string = ''
        eval_string = ''
        for index in range(1, len(line) - 1):
            if index % 2 == 1:
                if line[index] not in memory:
                    error = True
                else:
                    eval_string += str(memory[line[index]])
            else:
                eval_string += line[index]
            string += line[index] + ' '
            

        if error:
            print(string + ' = unknown')
        else:
            result = eval(eval_string)
            output = -1
            for key, value in memory.items():
                if value == result:
                    output = key
                    break
            if output == -1:
                output = 'unknown'
            print(string + ' = ' + output)
         
    else:
        memory = {}

    line = sys.stdin.readline()
