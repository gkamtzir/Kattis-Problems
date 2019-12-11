N = int(input())

for i in range(N):
    data = input()

    if data == "P=NP":
        print("skipped")
    else:
        print(eval(data))
