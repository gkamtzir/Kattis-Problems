import math

def narrow_down_coords(possible_x, possible_y, sub_quadkey):
    if sub_quadkey == "0":
        possible_x = [possible_x[0], math.floor((possible_x[0] + possible_x[1])/2)]
        possible_y = [possible_y[0], math.floor((possible_y[0] + possible_y[1])/2)]
    elif sub_quadkey == "1":
        possible_x = [math.ceil((possible_x[0] + possible_x[1])/2), possible_x[1]]
        possible_y = [possible_y[0], math.floor((possible_y[0] + possible_y[1])/2)]
    elif sub_quadkey == "2":
        possible_x = [possible_x[0], math.floor((possible_x[0] + possible_x[1])/2)]
        possible_y = [math.ceil((possible_y[0] + possible_y[1])/2), possible_y[1]]
    else:
        possible_x = [math.ceil((possible_x[0] + possible_x[1])/2), possible_x[1]]
        possible_y = [math.ceil((possible_y[0] + possible_y[1])/2), possible_y[1]]

    return possible_x, possible_y

s = input()
zoom = len(s)

possible_x = [0, 2**zoom - 1]
possible_y = [0, 2**zoom - 1]

index = 0

while possible_x[0] != possible_x[1]:
    possible_x, possible_y = narrow_down_coords(possible_x, possible_y, s[index])
    index += 1

print("%d %d %d" %(zoom, possible_x[0], possible_y[0]))
