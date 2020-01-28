import sys

end = 0

for line in sys.stdin:
    if line == "\n":
        end = 0
    else:
        count = 0
        for symbol in line:
            if symbol == "*":
                count += 1
        result = "." * end
        result += "*" * count
        end += count
        result += "." * (len(line) - 1 - end)
        print(result[::-1])
