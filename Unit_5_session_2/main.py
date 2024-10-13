# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a dp algorithm?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I will use dynamic programming for this problem. Set dp[i] as the amount of unique BST give i nodes

# base case
# dp[0] = 1 # no node -> 1 type of tree(empty tree)
# dp[1] = 1 # 1 node -> 1 type of tree(1 node tree)

# recurrence
# for i number of nodes, suppose having a structure with root node j s.t. 1 <= j <= i, 
# then left tree has j-1 nodes and right tree has i-j nodes. So then the amount of 
# unique BST give i nodes will be the combination of 
# (amount of unique BST give j-1 nodes) * (amount of unique BST give i-j nodes) 
# => dp[i] = dp[j-1] + dp[i-j]
# then dp[n] will be the amount of unique BST give n nodes



# Implement
# Translate the pseudocode into Python and share your final answer: 
def numTrees(self, n: int) -> int: 
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i + 1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[n]

# Review / Evaulate 
# n is max size of self.req at a time
# O(n^2) time looping through all possible j for each i up to n.
# O(n) space for storing each computation of dp[i] up to n.



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if the tree is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# Perform BFS and keep track of level,
# at each level if we find a leaf node(node with no right or left child, 
# then return level + 2 for next level and root level)

# Implement
# Translate the pseudocode into Python and share your final answer: 
from collections import deque
def minDepth(root) -> int:
        if not root: return 0
        # bfs 
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()  
                if node.left:
                    q.append(node.left)

                    if (not node.left.left and not node.left.right):
                        return level + 2
                if node.right:
                    q.append(node.right)
                    
                    if (not node.right.left and not node.right.right):
                        return level + 2
            level += 1  
        return level

# Review / Evaulate
# n is nodes in tree
# O(n) worst case need to check all nodes until last level
# O(n) time for storing all nodes into queue