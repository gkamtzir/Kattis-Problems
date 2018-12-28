N = input()
M = input()

if len(N) > len(M):
    zeros = len(N) - len(M)
    zeros = "0" * zeros
    M = zeros + M
elif len(N) < len(M):
    zeros = len(M) - len(N)
    zeros = "0" * zeros
    N = zeros + N

N = list(N)
M = list(M)

N_new = ""
M_new = ""

for index in range(len(N)):
    if N[index] > M[index]:
        M[index] = ""
        N_new += N[index]
    elif N[index] < M[index]:
        N[index] = ""
        M_new += M[index]
    else:
        N_new += N[index]
        M_new += M[index]
if N_new == "":
    print("YODA")
else:
    print(int(N_new))

if M_new == "":
    print("YODA")
else:
    print(int(M_new))
