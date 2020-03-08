def create_prefixes(phone_list):
    prefixes = {}
    for phone in phone_list:
        for i in range(1, len(phone)):
            prefix = phone[0:i]
            if prefixes.get(prefix) is None:
                prefixes[prefix] = []
            prefixes[prefix].append(phone)
    return prefixes

def check(prefixes, phone_list):
    for phone in phone_list:
        if prefixes.get(phone) is not None:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    n = int(input())
    phone_list = []
    for i in range(n):
        phone_list.append(input())
    print(check(create_prefixes(phone_list), phone_list))
