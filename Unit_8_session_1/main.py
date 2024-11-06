# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a dfs algorithm?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I first construct a graph for the emails and keep a dictionary to map each email to the account name. I will create an edge for 2 emails if they are under the same account.
# Then I will dfs through each email and add the emails that are in the same connected compoent to a temp array that I will sort and add to a result array. 
# I will then lastly combine the user's name and return the result array.

# Implement
# Translate the pseudocode into Python and share your final answer: 
from collections import defaultdict 
def accountsMerge(accounts):
        graph = defaultdict(set)
        f = {}
        for acc in accounts: 
            for email in range(1, len(acc)):
                f[acc[email]] = acc[0]
                for others in range(email, len(acc)):
                    graph[acc[email]].add(acc[others])
                    graph[acc[others]].add(acc[email])
        seen = set()
        def dfs(node, check):
            nonlocal seen
            seen.add(node)
            check.append(node)
            for i in graph[node]:
                if i not in seen:
                    dfs(i, check)
                    
        res = []
        for i in f:
            if i in seen:
                continue
            temp = [] 
            dfs(i, temp)
            res.append([f[i]] + sorted(temp))
        
        return res
            
# Review / Evaulate 
# n is number of total nodes, e is total number of edges.
# O((n + e)) time performing dfs with adj list
# O(n + e) space for storing all possible nodes in an undirected adj matrix



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if the root is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# I will dfs while storing a path array that keeps track of current nodes until I reach a leaf node. Then I will compute the sum of the path. This is used to 
# determine if the target sum is reached. If it is, then I will add this path array to the result array. Lastly I will return the result array.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def pathSum(root, targetSum: int):
    if not root: return []
    res = []
    def dfs(path, node):
        nonlocal res
        if not node: return
        
        if node.left:
            dfs(path + [node.left.val], node.left)

        if node.right:
            dfs(path + [node.right.val], node.right)
        
        if not node.left and not node.right:
            if sum(path) == targetSum:
                res.append(path)
    
    dfs([root.val], root)

    return res

# Review / Evaulate
# n is number of total nodes in the tree
# O(n) -> worse case I will travel through entire tree
# O(n) -> space for storing paths, which can be at most n nodes for each path to leaf in the tree