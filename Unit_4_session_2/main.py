# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a sliding window approach?
# - can the string be empty?

# Plan
# Write out in plain English what you want to do: 
# I will use a dynamic sliding window approach and keep a hashmap to keep track of frequencies of characters in the window.
# Scanning through the string, I will shrink the window whenever the frequencies of a character is over 1. This 
# allows me to find the longest substring w/o having a character repeating i.e. freq over 2.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def lengthOfLongestSubstring(s: str) -> int:
        if len(s) < 1:
            return 0
        
        l = 0
        res = 1
        f = {s[l] : 1}
        for r in range(1, len(s)):
            f[s[r]] = f.get(s[r], 0) + 1
            while f[s[r]] > 1: 
                f[s[l]] -= 1
                l += 1
            res = max(res, r-l+1) 
        return res

# Review / Evaulate 
# n is size of string
# O(n) time for looping through the array. The hashmap access is average O(1) and shrinking of window will be smaller than n. So total time complexixty is O(n)
# O(n) space, worse case we would store every character in the hashmap because all are unique



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - How should I check anagrams?
# - Are there any additional space constraints?

# Plan
# Write out in plain English what you want to do: 
# I will loop through each string in strs and set up frequencies map of each string (constant time with [0] * 26), 
# then keep a hashmap to check against the frequencies. If the frequencies is seen before, then add current string
# to that list, else add a list with the current string. Thus, res.values will be the solution.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def groupAnagrams(strs):
    res = {}
    for i in strs:
        sort = [0] * 26
        for j in i:
            sort[ord(j) - ord('a')] += 1
        sort = tuple(sort)
        if sort in res:
            res[sort].append(i)
        else:
            res[sort] = [i]
    
    return res.values()

# Review / Evaulate
# n is size of strs, m is size of hashmap (worse case will be every string in strs)
# O(n * 26 * m) -> O(n^2) time for looping through strs and checking each frequencies mapping with mappings in hashmap
# O(m) -> O(n) space for storing each string in strs to the hashmap