# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use greedy?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I will perform a greedy approach. I notice that max profit is equal to getting sum of all valley and immediate peak. 
# First, I will declare a profit variable, then to get all the vallys (all number before it is greater than itself) I will use a counter and increment through prices. 
# After finding a valley, I will incremnt pointer again to determine the peak(where all numbers before it is less than itself.)
# Then I will increment difference between the valley and the peak into profit.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def maxProfit(prices) -> int:
    n = len(prices)     
    valley = prices[0]
    peak = prices[0]
    i = 0
    profit = 0
    while i < n - 1:
        while i < n - 1 and prices[i] >= prices[i+1]: # valley
            i += 1

        valley = prices[i] # prices[i] < prices[i+1]

        while i < n - 1 and prices[i] < prices[i + 1]: # peak
            i += 1

        peak = prices[i] # prices[i] >= prices[i+1]
        profit += peak - valley
        
    return profit 
         
# Review / Evaulate 
# n is number of stock prices
# O(n) for going through every element in price.
# O(1) space for storing constant variables



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if there nums is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do:  
# I will continue with a greedy approach, first I declare a set for all elements in nums, and length variable to store maximum length. 
# Then for every element in nums, I check if there its previous number is already in nums. If the previous number is in the set, 
# then I know that I can skip this number because its previous number will give me a larger consequtive length. 
# Now if the number-1 is not in the set, then I can try to record the consequence starting with it by checking if
# it + 1 is in nums and incrementing it until it + 1 is not longer in nums. Then record maximum length and return length at the end of iterations.


# Implement
# Translate the pseudocode into Python and share your final answer: 
def longestConsecutive(nums) -> int:
    nums = set(nums)
    length = 0
    for i in nums:
        if i-1 not in nums:
            temp = 1
            while (i+temp) in nums:
                temp += 1
            length = max(length, temp)
    return length

# Review / Evaulate
# n is length of nums
# O(n) for looping through all elements in array and creating set out of nums.
# O(n) because storing up to n elements with the set.