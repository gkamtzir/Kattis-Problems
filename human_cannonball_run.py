import sys, math

def min_distance(n, distances, visited): 
    min = sys.maxsize 
   
    for v in range(n): 
        if distances[v] < min and visited[v] == False: 
            min = distances[v] 
            min_index = v 
  
    return min_index

def dijkstra(n, graph, src): 
    distances = [sys.maxsize] * n 
    distances[src] = 0
    visited = [False] * n
  
    for i in range(n): 
  
        u = min_distance(n, distances, visited) 
   
        visited[u] = True
   
        for v in range(n): 
            if graph[u][v] > 0 and visited[v] == False and distances[v] > distances[u] + graph[u][v]: 
                distances[v] = distances[u] + graph[u][v] 
  
    return distances[n - 1]

points = []
points.append(list(map(float, input().split())))
end = list(map(float, input().split()))

n = int(input())

graph = [[0 for column in range(n + 2)] for row in range(n + 2)]

for i in range(n):
    points.append(list(map(float, input().split())))

points.append(end)

for i in range(n + 2):
    for j in range(i, n + 2):
        if i == j:
            graph[i][j] = 0
        elif i == 0 or j == 0:
            distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            graph[i][j] = distance / 5 
            graph[j][i] = distance / 5
        else:
            distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if distance >= 50:
                cost = 2 + (distance - 50) / 5
            elif distance >= 30:
                cost = 2 + (50 - distance) / 5
            else:
                cost = distance / 5
            graph[i][j] = cost
            graph[j][i] = cost

print(dijkstra(n + 2, graph, 0))
