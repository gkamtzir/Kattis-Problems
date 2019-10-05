def check_traps(terrain, width, height, i, j):
    if i - 1 >= 0:
        if terrain[i - 1][j] == "T":
            return True
    if i + 1 < height:
        if terrain[i + 1][j] == "T":
            return True
    if j - 1 >= 0:
        if terrain[i][j - 1] == "T":
            return True
    if j + 1 < width:
        if terrain[i][j + 1] == "T":
            return True

def check_moves(terrain, width, height, i, j):
    moves = ["N", "W", "S", "E"]
    if i - 1 >= 0:
        if terrain[i - 1][j] == "#":
            moves.remove("N")
    else:
        moves.remove("N")
    if i + 1 < height:
        if terrain[i + 1][j] == "#":
            moves.remove("S")
    else:
        moves.remove("S")
    if j - 1 >= 0:
        if terrain[i][j - 1] == "#":
            moves.remove("W")
    else:
        moves.remove("W")
    if j + 1 < width:
        if terrain[i][j + 1] == "#":
            moves.remove("E")
    else:
        moves.remove("E")
    return moves

def move(terrain, i, j, direction):
    if direction == "N":
        return i - 1, j
    if direction == "E":
        return i, j + 1
    if direction == "S":
        return i + 1, j
    if direction == "W":
        return i, j - 1

W, H = map(int, input().split())

terrain = []
visited = []

# Initializing the terrain
# and the visited list.
for i in range(H):
    line = input()
    terrain.append([])
    visited.append([])
    
    j = line.find("P")
    if j != -1:
        pos = [i, j]
    for char in line: 
        terrain[i].append(char)
        visited[i].append(False)

# Initializing the history stack.
stack = []
stack.append(pos)

# Initializing the available moves
# for each position.
moves = []
moves.append(check_moves(terrain, W, H, pos[0], pos[1]))

gold_counter = 0

# Main loop.
while len(stack) != 0:
    pos = stack[len(stack) - 1]
    # If there are traps we fall back
    # to the previous position.
    if check_traps(terrain, W, H, pos[0], pos[1]):
        stack.pop()
        moves.pop()
        continue
    available_moves = moves[len(moves) - 1]
    # If there are no available moves
    # we fall back to the previous position.
    if len(available_moves) == 0:
        stack.pop()
        moves.pop()
    else:
        while len(available_moves) > 0:
            next_move = available_moves.pop()
        
            next_i, next_j = move(terrain, pos[0], pos[1], next_move)
            # If the new position is visited
            # we try to move to the next available
            # position.
            if visited[next_i][next_j]:
                continue
            else:
                # If the new position contains gold
                # we take it.
                if terrain[next_i][next_j] == "G":
                    gold_counter += 1
                    
                # Marking the new position as visited.
                visited[next_i][next_j] = True
                
                # Adding it to the history
                stack.append([next_i, next_j])
                
                # Updating the moves of the previous position.
                moves[len(moves) - 1 ] = available_moves
                
                # Adding the moves of the new position.
                moves.append(check_moves(terrain, W, H, next_i, next_j))
                break
       
print(gold_counter)
