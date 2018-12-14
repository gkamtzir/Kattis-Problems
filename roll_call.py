import operator, sys

def sort_by_name_same_lastnames(names):
    names = sorted(names, key = operator.itemgetter(1))
    start = 0
    count = 1
    last_name = names[0][1]
    for i in range(1, len(names)):
        if last_name == names[i][1]:
            count += 1
        else:
            if count > 1:
                names[start:i] = sorted(names[start:i], key = operator.itemgetter(0))
            start = i
            count = 1
            last_name = names[i][1]
    if count > 1:
        names[start:] = sorted(names[start:], key = operator.itemgetter(0))
    return names

name = sys.stdin.readline()
names = []
name_history = []
duplicates = []
while name:
    name = name[:len(name) - 1].split(' ')
    names.append((name[0], name[1]))
    if name[0] not in name_history:
        name_history.append(name[0])
    else:
        if name[0] not in duplicates:
            duplicates.append(name[0])
    name = sys.stdin.readline()

names = sort_by_name_same_lastnames(names)
for name in names:
    if name[0] in duplicates:
        print(name[0], name[1])
    else:
        print(name[0])
