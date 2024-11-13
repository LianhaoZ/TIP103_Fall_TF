# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - Are there any space constraints?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# maximum subarray is the maximum accumlated sum. Since negatives were possible in the array, if subarray is negative, I will reset the cursum to be 0(starting at this point)

# Implement
# Translate the pseudocode into Python and share your final answer: 
def maxSubArray(nums) -> int:
    curmax = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        if curmax < 0:
            curmax = 0
        curmax += nums[i]
        res = max(res, curmax)
    return res 
            
# Review / Evaulate 
# n is length of numbers
# O(n) time for looping through array 
# O(1) space for 2 constant variables 



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if the string is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# Expand from the center, and check max palindrome that can be formed or each index. Need to check for case where there is one element in the center versus 2 element in the center. 
# This is handled with expadning with current index and expanding with index i and i-1.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def longestPalindrome(s: str) -> str:
        def expand_center(l, r): 
            while l >= 0 and r < len(s) and s[l] == s[r]:  
                l -= 1
                r += 1   
            return r-l+1, [l+1, r]

        total = 0
        res = [0, 0]
        for i in range(len(s)):
            curmax, string = expand_center(i-1, i) # even length looking at i.e. aa
            curmax1, string1 = expand_center(i, i)   #odd length looking at i.e. aba

            if curmax > total: 
                total = curmax  
                res = string 
            if curmax1 > total: 
                total = curmax1
                res = string1  
        
        return s[res[0]:res[1]]
                  

# Review / Evaulate
# n is number of answers
# O(n^2) b/c looping through each index in the string, and expanding from center will worst case be O(n).
# O(n) because copying string for the returned string, worst case copies whole string, which takes O(n) space.