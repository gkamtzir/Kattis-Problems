import sys
import copy

def min_distance(n, distances, visited): 
    min_value = sys.maxsize
    min_index = None
   
    for v in range(n): 
        if distances[v] < min_value and visited[v] == False: 
            min_value = distances[v] 
            min_index = v 
      
    return min_index

def dijkstra(n, graph, src): 
    distances = [sys.maxsize] * n 
    distances[src] = 0
    visited = [False] * n
    path = [[0]] * n
  
    for i in range(n):
        u = min_distance(n, distances, visited)
        if u is None:
            continue
   
        visited[u] = True
   
        for v in range(n): 
            if graph[u][v] > 0 and visited[v] == False and distances[v] > distances[u] + graph[u][v]: 
                distances[v] = distances[u] + graph[u][v]
                path[v] = path[u][:]
                path[v].append(v)

    return path[n - 1]

def yen_ksp(graph, n, src, sink):
    A = []
    A.append(dijkstra(n, graph, src))
    B = []
    for k in range(1, 4):
        for i in range(0, len(A[k - 1]) - 2):
            temp_graph = copy.deepcopy(graph)
            
            spur_node = A[k - 1][i]
            #print(A[k-1])
            root_path = A[k - 1][0:i+1]

            for path in A:
                #print(path[0:i + 1])
                #print(root_path)
                check = [l for l, j in zip(root_path, path[0:i + 1]) if l == j]
                #print(check)
                #print("-----")
                if len(check) == len(root_path):
                    temp_graph[path[i]][path[i + 1]] = 0

            for node in root_path:
                if node != spur_node:
                    temp_graph[node] = [0] * n
                    for _ in range(len(temp_graph)):
                        temp_graph[_][node] = 0
            print(temp_graph)
            spur_path = dijkstra(len(temp_graph), temp_graph, spur_node)

            total_path = spur_path
            print(spur_path)
            if total_path not in B:
                B.append(total_path)
        if len(B) == 0:
            break
        B = sorted(B)
        print(f"B {B}")
        A.append(B[0])
        B.pop()
    return A
         
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ];

#print(dijkstra(9, graph, 0))
print(yen_ksp(graph, 9, 0, 8))
