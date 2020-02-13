import sys

def evaluate(operand1, operand2, operation):
    if operand1 is None or operand2 is None:
        return "undefined"
    
    if operation == "=":
        return str(int(operand1) == int(operand2)).lower()
    elif operation == "<":
        return str(int(operand1) < int(operand2)).lower()
    else:
        return str(int(operand1) > int(operand2)).lower()

memory = {}

for command in sys.stdin:
    command = command[:len(command) - 1].split()
    command_type = command[0]
    if command_type == "define":
        memory[command[2]] = command[1]
    else:
        print(evaluate(memory.get(command[1]), memory.get(command[3]), command[2]))
