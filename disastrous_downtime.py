import heapq

n, k = map(int, input().split())

server = [0] * k
heapq.heapify(server)

for i in range(n):
    request = int(input())
    found = False
    if request < server[0]:
        for j in range(k):
            heapq.heappush(server, 0)
        heapq.heapreplace(server, request + 1000)
    else:
        heapq.heapreplace(server, request + 1000)

print(int(len(server) / k))
