# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use bfs?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I will collect the coordinates for all the 0s.
# Then I will BFS based on those coordinates Collectively or all at once to all the rest of the coordinates 
# in the result matrix, mark each level as previous value + 1 and don't check again via keeping a seen set.


# Implement
# Translate the pseudocode into Python and share your final answer: 
from collections import deque
def updateMatrix(mat):
    m = len(mat)
    n = len(mat[0])
    zero = []
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                zero.append((r,c))
    
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    def bfs(z): 
        ans = [[0]*n for _ in range(m)]
        q = deque(z)
        seen = set(z)  
        while q:
            x, y = q.popleft() 
            for newr, newc in dirs:
                nx = x + newr
                ny = y + newc
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen: 
                    seen.add((nx,ny)) 
                    ans[nx][ny] = ans[x][y] + 1 
                    q.append((nx, ny))  
        return ans
        

    return bfs(zero)

# Review / Evaulate 
# n is number of rows, m is number of cols
# O(n * m) time looping through all possible rows and cols values in the matrix
# O(n * m) space for storing each value in the matrix 



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if the matrix is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# I will dfs to each of the 4 directions and change the color of the image to the given color if the color in the image
# if the same as the original color. Some edge cases include when there is when image is empty then just return empty. Or 
# if image is already set to the right color at the start, then there is no need to continue. I will also keep a seen set to prevent traversing visited cells. 

# Implement
# Translate the pseudocode into Python and share your final answer: 
def floodFill(image, sr: int, sc: int, color: int):
    row = len(image)
    col = len(image[0])
    original = image[sr][sc]

    seen = set()
    def dfs(x, y): 
        nonlocal seen
        if x > row - 1 or y > col - 1 or x < 0 or y < 0 or image[x][y] != original or (x,y) in seen:
            return

        seen.add((x, y))
        
        if image[x][y] == original:
            image[x][y] = color
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        

    if image[sr][sc] == color: 
        return image
    if len(image)==0: 
        return []

    dfs(sr, sc)
    return image

        

        

# Review / Evaulate
# n is number of rows, m is number of cols
# O(n * m) time looping through all possible rows and cols values in the matrix
# O(n * m) space for storing each value in the matrix 