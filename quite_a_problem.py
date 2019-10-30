import sys, re

pattern = "^.*(problem).*$"

for line in sys.stdin:
    line = line[:len(line) - 1].lower()
    if re.match(pattern, line):
        print("yes")
    else:
        print("no")
