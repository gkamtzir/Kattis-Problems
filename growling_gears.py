test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    max_torque = -1
    gear = -1
    for j in range(n):
        a, b, c = map(int, input().split())
        # This formula originates from the derivative of
        # the parabola which is set to equal zero.
        torque = (b**2)/(4*a) + c
        if torque > max_torque:
            max_torque = torque
            gear = j + 1
    print(gear)
