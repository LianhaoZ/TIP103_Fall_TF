# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use dfs?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# For each value on the board, I will dfs to check if it is possible to generate a path such that the word formed by the path matches the given word.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def exist(board, word: str) -> bool:
    directions = [(1, 0), (0, -1),(-1, 0), (0, 1)]
    m = len(board)
    n = len(board[0])
    visited = set()

    def dfs(r, c, visited, idx):   
        if idx == len(word):
            return True 

        if 0 > r or r > m - 1 or 0 > c or c > n - 1 or (r,c) in visited or board[r][c] != word[idx]: 
            return False

        visited.add((r,c)) 
        ans = False
        for x, y in directions:   
            if dfs(r + x, c + y, visited, idx + 1):
                ans = True

        visited.remove((r,c)) 
        return ans

        
        
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]: 
                ans = dfs(i,j, visited, 0)  
                if ans:
                    return True  
    return False     

# Review / Evaulate 
# n is number of rows, m is number of cols, L is length of word
# O(n*m * 4^L) time for dfs at each coordinate for each word
# O(L) space for storing each coordinate at each coordiante



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if there n is 0?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do:  
# I will backtrack. At each step I have the option to add a closing or a opening bracket. If # of opening brackets are less than n(half of string), then I can continue to add opening brackets. If # of closing brackets are less than number of opening brackets, I can also continue to add closing brackets. When my step/string length reaches 2n, then I can return and add a copy of the string to answer array to return.
# initalize target string length, which is 2 times n.
# initalize answer array
# initalize path array of size 2n.
# define dfs function, where I take in starting index and number of opening brackets.
#       check if current index or stringing length is at 2n, if so copy the current path and return
#       if number of opening brackets is less than n
#            add a opening braket to path and dfs with increased string length/index and increased opening bracket count
#       if number of closing bracket is less than opening
#           add a closing braket to path and dfs with increased string length/index and same opening bracket count
# perform dfs starting at string length 0/index 0 and 0 opening brakcets.
# return the answer array

# Implement
# Translate the pseudocode into Python and share your final answer: 
def generateParenthesis(n: int):
    m = 2 * n
    ans = []
    path = [''] * m
    def dfs(i, open):
        if i == m:
            ans.append(''.join(path.copy()))
            return

        if open < n: #number of opening can't exceed n
            path[i] = '('
            dfs(i + 1, open + 1) 
        if i - open < open: # number of closing can't exceed opening 
            path[i] = ')'
            dfs(i + 1, open) 
        
    dfs(0, 0)
    return ans         

# Review / Evaulate
# O(n*C(n)) where C is catalan's number(ways to bracket n paires of items in this case brackets) b/c generating valid combinations will take C(n) and for each valid combination recreating the string will be O(n). Also the catalan number represents number of distinct binary search trees that can be constructed with 𝑛  distinct keys
# O(n*C(n)) because storing up to C(n) valid combinations and each combination takes 2n of space.