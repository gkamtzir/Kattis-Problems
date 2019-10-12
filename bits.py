test_cases = int(input())

# For each test case.
for i in range(test_cases):
    number = input()
    maximum = -1
    for j in range(len(number)):
        # Fetching the new substring.
        integer = number[:j + 1]
        counter = 0
        # Converting to binary.
        binary = bin(int(integer))[2:]
        for bit in binary:
            if bit == "1":
                counter += 1
        if counter > maximum:
            maximum = counter
    print(maximum)
    
