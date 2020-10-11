def check_password(S, P):
    if S == P:
        return "Yes"
    if len(P) + 1 == len(S):
        if S[:-1] == P and S[-1].isdigit():
            return "Yes"
        if S[1:] == P and S[0].isdigit():
            return "Yes"
    if S == reverse_case(P):
        return "Yes"
    return "No"

def reverse_case(P):
    reversed_case = ''
    for letter in P:
        if letter.islower():
            reversed_case += letter.upper()
        else:
            reversed_case += letter.lower()
    return reversed_case

S = input()
P = input()

print(check_password(S, P))
