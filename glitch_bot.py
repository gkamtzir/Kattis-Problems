# Calculates the end point based on
# the given instructions.
def calculate_route(instructions):
    x = 0
    y = 0
    direction_index = 0

    directions = ["N", "E", "S", "W"]

    for instruction in instructions:
        if instruction == "Right":
            direction_index = (direction_index + 1) % len(directions)
        elif instruction == "Left":
            direction_index = (direction_index - 1) % len(directions)
        else:
            x, y = move(x, y, directions[direction_index])
    return x, y

# Moves the bot based on current position
# and direction.
def move(x, y, direction):
    if direction == "N":
        y += 1
    elif direction == "S":
        y -= 1
    elif direction == "E":
        x += 1
    else:
        x -= 1
    return x, y

# Reading parameters.
x, y = map(int, input().split())
n = int(input())

instructions = []
movements = ["Forward", "Right", "Left"]

# Reading input.
for i in range(n):
    instructions.append(input())

done = False

for i in range(len(instructions)):
    for movement in movements:
        if movement != instructions[i]:
            temp_instructions = instructions[:]
            temp_instructions[i] = movement
            # Calculating end point.
            temp_x, temp_y = calculate_route(temp_instructions)
            # If end point matches the desired one
            # then we're done.
            if temp_x == x and temp_y == y:
                print(f"{i+1} {movement}")
                done = True
                break
    if done:
        break
