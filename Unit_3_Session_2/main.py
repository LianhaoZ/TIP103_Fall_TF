# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can the array be empty?
# - does the target always exist in array

# Plan
# Write out in plain English what you want to do: 
# I will perform binary search, finding middle point and checkign against target, if middle value of array is greater than targer, I will check set the lowerbound to mid + 1, and vice versa to set upperbound to mid-1. 

# Implement
# Translate the pseudocode into Python and share your final answer: 
def search(nums, target):
  l , r = 0, len(nums)-1
  while l <= r:
      mid = (l+r) // 2
      if nums[mid] > target:

          r = mid - 1
      elif nums[mid] < target:
          l = mid + 1
      else:
          return mid
  return -1


# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - can the total versions be 0?
# - Are there any additional space constraints?

# Plan
# Write out in plain English what you want to do: 
# I will binary search and check midpoint at each iteration

# Implement
# Translate the pseudocode into Python and share your final answer: 
def firstBadVersion(n):
  l, r = 1, n 
  while l<r:
      mid = (l+r)//2
      if isBadVersion(mid): 
          # If mid point is bad then there might be more bad versions before it, shift right pointer and check for earlier bad version.
          r = mid
      else:
          # If mid point is good then we know that everything to the left is good, shift left pointer to check for bad version in right half
          l = mid + 1
  return r 


# PROBLEM 3
# Understand
# Share 2 questions you would ask to help understand the question:
# - can x be less than 1
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# use binary search to obtain midpoint, which is checked at each iteration against x/mid. If equal then mid ** 2 equals x, which means x ** 0.5 equals mid.

# Implement
# Translate the pseudocode into Python and share your final answer: 
def mySqrt(x):
  l,r = 1, x
  while l <= r:
      mid = (l+r)//2 
      if mid == x // mid:
          return mid
      elif mid > x // mid:
          r = mid - 1
      else:
          l = mid + 1
  # Return the right pointer for the closes number to square for our target as it is the last remaining valid number.
  return r




