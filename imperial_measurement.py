def calculate_forward(converter, from_index, to_index, value):
    for i in range(from_index, to_index):
        value = value * converter[i]["value"]
    return value


def calculate_backward(converter, from_index, to_index, value):
    converter.reverse()
    for i in range(from_index + 1, to_index + 1):
        value = value / converter[i]["value"]
    return value

def find_index(coverter, unit):
    for i in range(len(converter)):
        if converter[i]["name"] == unit or converter[i]["short_name"] == unit:
            return i
        
# Defining the converter structure.      
converter = [
    {
        "name": "league",
        "short_name": "lea",
        "value": 3
    },
    {
        "name": "mile",
        "short_name": "mi",
        "value": 8
    },
    {
        "name": "furlong",
        "short_name": "fur",
        "value": 10
    },
    {
        "name": "chain",
        "short_name": "ch",
        "value": 22
    },
    {
        "name": "yard",
        "short_name": "yd",
        "value": 3
    },
    {
        "name": "foot",
        "short_name": "ft",
        "value": 12
    },
    {
        "name": "inch",
        "short_name": "in",
        "value": 1000
    },
    {
        "name": "thou",
        "short_name": "th",
        "value": 3
    }
]

data = input().split()

# Mapping the data accordingly.
value = int(data[0])
from_unit = data[1]
to_unit = data[3]

# Locating each item in the 'converter' list.
from_index = find_index(converter[:], from_unit)
to_index = find_index(converter[:], to_unit)

if from_index < to_index:
    print(calculate_forward(converter[:], from_index, to_index, value))
else:
    print(calculate_backward(converter[:], len(converter) - 1 - from_index, len(converter) - 1 - to_index, value))

