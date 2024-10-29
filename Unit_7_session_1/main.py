# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use topological sorting algorithm?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I tolopologically sort the graph and check for indegree. Then I loop through via a queue keeping track and only 
# visit the nodes with 0 indegrees(all preqs met). I will record the order I visit the nodes via a array.

# Implement
# Translate the pseudocode into Python and share your final answer: 
from collections import deque
def findOrder(numCourses: int, prerequisites):
    idegree = [0] * numCourses
    adj = [[] for x in range(numCourses)]
    
    #check indegree
    for prereq in prerequisites:
        idegree[prereq[0]] += 1
        adj[prereq[1]].append(prereq[0]) 

    q = deque()
    for i in range(numCourses):
        if idegree[i] == 0:
            q.append(i)
    
    visited = []
    while q:
        node = q.popleft()
        visited.append(node)
        for neighbor in adj[node]:
            idegree[neighbor] -= 1
            if idegree[neighbor] == 0:
                q.append(neighbor)

    return visited if len(visited) == numCourses else []
         


# Review / Evaulate 
# n is number of total nodes, v is total edges.
# O(n + e) time looping through all possible nodes + edges
# O(n + e) space for storing all possible nodes and edges in adj matrix



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - What if there were no prereqs for a class?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# I will first collect all the prereqs for each accesa via hashmap. Then for each course I will perform bfs to check all the nodes I have visited.
# This will be kept tracked of via binary T/F array. For each query, then i can check if one course can be reached from another in O(1).

# Implement
# Translate the pseudocode into Python and share your final answer: 
def checkIfPrerequisite(numCourses: int, prerequisites, queries):
    ans = [False] * len(queries)
    adj = [[False] * numCourses  for _ in range(numCourses)] 
    inital = {i:[] for i in range(numCourses)}

    for prereq in prerequisites: 
        inital[prereq[0]].append(prereq[1]) 

    for i in range(numCourses):
        q = deque()
        q.append(i)
        while q:
            node = q.popleft()  
            adj[i][node] = True
            for j in inital[node]:
                if not adj[i][j]:                         
                    q.append(j)

    for i, val in enumerate(queries):
        x = val[0]
        y = val[1]
        if adj[x][y]:
            ans[i] = True 
            
    return ans    
 

# Review / Evaulate
# n is total number of courses, e is total edges
# O(n*(n + e)) worst case when all course might be connected to all other courses for bfs
# O(n*n) space for storing all nodes in adj matrix