import sys

modulo = []

for i in range(10):
    number = int(sys.stdin.readline())
    mod = number % 42
    if mod not in modulo:
        modulo.append(mod)

print(len(modulo))
