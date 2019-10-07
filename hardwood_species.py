import sys

tree_dict = {}
total = 0

for line in sys.stdin:
    name = line[:len(line) - 1]
    total += 1
    if tree_dict.get(name) is None:
        tree_dict[name] = 1
    else:
        tree_dict[name] += 1

for key in sorted(tree_dict):
    print(f"{key} {(tree_dict[key]/total) * 100:.6f}")
