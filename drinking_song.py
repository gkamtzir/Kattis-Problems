def print_verse(beverage, N):
    print(f"{N} { 'bottles' if N > 1 else 'bottle' } of {beverage} on the wall, {N} { 'bottles' if N > 1 else 'bottle'} of {beverage}.")    
    first_part = f"Take { 'one' if N > 1 else 'it'} down, pass it around,"
    second_part = f"{N - 1} {'bottles' if N - 1 > 1 else 'bottle'} of {beverage} on the wall."
    print(f"{first_part} {second_part if N > 1 else f'no more bottles of {beverage}.'}\n")

N = int(input())

word = input()

for i in range(N, 0, -1):
    print_verse(word, i)
