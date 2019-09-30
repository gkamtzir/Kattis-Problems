def to_decimal(number, system, base):
    exp = 0
    total = 0
    for char in number[::-1]:
        total += system[char] * base ** exp
        exp += 1
    return total

def from_decimal(number, system_list, base):
    div = number // base
    mod = number % base
    indices = [mod]
    number = div
    while number != 0:
        div = number // base
        mod = number % base
        number = div
        indices.append(mod)
    return ''.join([system_list[index] for index in indices[::-1]])
        

T = int(input())

for i in range(T):
    alien_number, source_language, target_language = map(str, input().split())
    system = {}
    system_list = []
    source_base = 0
    for char in source_language:
        system[char] = source_base
        source_base += 1
    for char in target_language:
        system_list.append(char)
    decimal = to_decimal(alien_number, system, source_base)
    print(f'Case #{i+1}: {from_decimal(decimal, system_list, len(system_list))}')
    
