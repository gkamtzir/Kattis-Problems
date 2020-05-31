def mark_to_deg(mark_difference):
    return mark_difference * 9

def get_difference(initial, final, counter_clockwise = True):
    absolute_difference = abs(initial - final)
    if counter_clockwise:
        if final > initial:
            return absolute_difference
        else:
            return 40 - absolute_difference
    else:
        if final > initial:
            return 40 - absolute_difference
        else:
            return absolute_difference
            

initial, first, second, third = map(int, input().split())

while initial != 0 or first != 0 or second != 0 or third != 0:
    total_degrees = 720
    total_degrees += mark_to_deg(get_difference(initial, first, False))
    total_degrees += 360
    total_degrees += mark_to_deg(get_difference(first, second))
    total_degrees += mark_to_deg(get_difference(second, third, False))
    print(total_degrees)
    initial, first, second, third = map(int, input().split())
