T = int(input())

layout = {
    "1": {
        "x": 0,
        "y": 0
    },
    "2": {
        "x": 0,
        "y": 1 
    },
    "3": {
        "x": 0,
        "y": 2 
    },
    "4": {
        "x": 1,
        "y": 0 
    },
    "5": {
        "x": 1,
        "y": 1 
    },
    "6": {
        "x": 1,
        "y": 2 
    },
    "7": {
        "x": 2,
        "y": 0 
    },
    "8": {
        "x": 2,
        "y": 1 
    },
    "9": {
        "x": 2,
        "y": 2 
    },
    "0": {
        "x": 3,
        "y": 1 
    }
}

data = {}

for i in range(201):
    number = str(i)
    previous = {
        "x": -1,
        "y": -1,
    }
    ok = True

    for digit in number:
        if not (layout[digit]["x"] >= previous["x"] and layout[digit]["y"] >= previous["y"]):
            ok = False
            break
        previous["x"] = layout[digit]["x"]
        previous["y"] = layout[digit]["y"]

    if ok:
        data[str(i)] = True

for i in range(T):
    number = input()

    if data.get(number) is not None:
        print(number)
    else:
        i = 1
        while True:
            if data.get(str(int(number) - i)) is not None:
                print(str(int(number) - i))
                break
            if data.get(str(int(number) + i)) is not None:
                print(str(int(number) + i))
                break
            i += 1 