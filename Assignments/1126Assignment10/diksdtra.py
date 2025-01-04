import heapq

def dijkstra(n, edges, s, t):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))#构建邻接表
    pq = [(0, s)]  # (distance, node)
    visited = set()
    distances = [float('inf')] * n
    distances[s] = 0
    while pq:#遍历节点
        dist, node = heapq.heappop(pq)
        if node == t:return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:#走到一个节点-->探路边上的邻居
            if neighbor not in visited:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    new_dist = dist+weight#更新距离
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
    return -1
n, m, s, t = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
# Solve the problem and print the result
result = dijkstra(n, edges, s, t)
print(result)