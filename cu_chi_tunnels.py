N = int(input())
D = list(map(int, input().split()))

pending_connections = 2

for item in D:
    if pending_connections == 0:
        pending_connections = -1
        break
    pending_connections -= 1
    pending_connections += item - 1

if pending_connections == 0:
    print("YES")
else:
    print("NO")
