n = int(input())

while n != 0:
    menu = {}
    for _ in range(n):
        order = list(map(str, input().split()))
        name = order[0]
        order = order[1:]
        for food in order:
            if food not in menu:
                menu[food] = []
            if name not in menu[food]:
                menu[food].append(name)
    for food in sorted(menu.keys()):
        print(food, end = ' ')
        for name in sorted(menu[food]):
            print(name, end = ' ')
        print('')
    print('')

    n = int(input())
