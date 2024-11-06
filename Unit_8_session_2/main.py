# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a dijkstra algorithm?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I first construct the graph using a adjacency matrix, keeping weight as the value of 2 nodes. Then I compute the longest time to complete the shortest
# path to any node. This is done via dijkstra and taking the maximum of resulting distance from source node k.

# Implement
# Translate the pseudocode into Python and share your final answer: 
import heapq
def networkDelayTime(times, n: int, k: int) -> int:
    g = [[-1]*n for _ in range(n)] 
    for x , y , w in times:
        g[x-1][y-1] = w


    dist = [float('inf')] * n
    def dijkstra(src):
        pq = [(0, src)] 
        dist[src] = 0
        while pq:
            current_dist, u = heapq.heappop(pq)

            for v in range(n):  
                if g[u][v] != -1:
                    weight = g[u][v] 
                    if dist[v] > current_dist + weight: 
                        dist[v] = current_dist + weight
                        heapq.heappush(pq, (dist[v], v))

    dijkstra(k - 1) 
    res = 0
    for i in dist:
        if i == float('inf'):
            return -1
        res = max(res, i)
    return res
            

            
# Review / Evaulate 
# n is number of total nodes, e is total number of edges.
# O((n*n) log n) time performing dijkstra with priority queue for worst case dense graph, average O((n+e)log n)
# O(n * n) space for storing all possible nodes in an adj matrix



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if the graph is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# For each newly added edge, I will add the edge to the adjacency list and then dfs to check if there is a connect component/cycle. 
# If so then I return the added edge.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def findRedundantConnection(edges):
    def dfs(graph, node, seen, prev): 
        if node in seen:
            return False
        seen.add(node)
        check = True
        for i in graph[node]: 
            if i == prev:
                continue
            if not dfs(graph, i, seen, node):
                check = False
        return check
        
    g = {i:[] for i in range(1000)}
    for prereq in edges: 
        g[prereq[0]-1].append(prereq[1]-1) 
        g[prereq[1]-1].append(prereq[0]-1) 
        seen = set()
        if not dfs(g, prereq[0]-1, seen, None):
            return prereq   
 

# Review / Evaulate
# n is number of total nodes (max will be 1000, so set to 1000), e is total number of edges.
# O(e * (n + e)) -> O(e * (1000 + e)) -> O(e * (e)) need to check all nodes with dfs with each added edge  
# O(n+e) -> O(e) space for storing all edges for each node in adj list, n is constant at 1000