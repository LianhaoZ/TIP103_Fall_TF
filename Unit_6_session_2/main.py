# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a dfs algorithm?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I first constructed a bidirectonal graph. Then through dfs I visited each neightbor. To record the number of 
# Connected compoenents I increment whenever the visited array was increased after dfs thrugh the node.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def findCircleNum(isConnected) -> int:
    g = {}
    n = len(isConnected) 
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1:
                if i not in g:
                    g[i] = []
                if j not in g:
                    g[j] = []
                if j not in g[i]: 
                    g[i].append(j)
                if i not in g[j]:
                    g[j].append(i)
    
    vis = set()
    def dfs(node):
        if node in vis:
            return 
        
        vis.add(node)  
        
        for neigh in g[node]:
            dfs(neigh)
        
    cur = cnt = 0
    while len(vis) < n:
        past = len(vis) 
        dfs(cur)  
        if len(vis) > past:
            cnt += 1 
        cur += 1
    return cnt


# Review / Evaulate 
# n is number of total nodes
# O(n) time looping through all possible nodes
# O(n * n) space for storing all possible nodes in a bidirectional adj matrix



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if the graph is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# I will dfs for the node and create a new node at each iteration. I will keep a visited dictionary and check every neighbor of current node
# if the neighbor has not been visited before, I will recurse with dfs to visit it and create it as a new node. Or else the neighbor has been created as a new node so 
# I will just add it to the current node's neighbors. At the end I return the curnode I have created.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def cloneGraph(node):
    def dfs(node, visited):
        if node is None:
            return None
        
        newNode = Node(node.val)
        visited[node.val] = newNode
        
        for adjNode in node.neighbors:
            if adjNode.val not in visited:
                newNode.neighbors.append(dfs(adjNode, visited))
            else:
                newNode.neighbors.append(visited[adjNode.val])
        
        return newNode
    
    return dfs(node, {})    
 

# Review / Evaulate
# n is nodes in graph
# O(n * n) need to check all nodes
# O(n * n) time for storing all nodes in adj list