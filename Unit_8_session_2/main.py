# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use the sorting function?
# - are there any time constraints? 

# Plan
# Write out in plain English what you want to do: 
# I will create a sorting function that given 2 numbers A, B, greedily compute if combining AB or BA will give the bigger number and order than as such. 
# Then using the sorting function I can sort the elements in num and return the sorted answer at the end.

# Implement
# Translate the pseudocode into Python and share your final answer: 
from functools import cmp_to_key
def largestNumber(nums):
    def compare(a, b): 
        ab = str(a) + str(b)   
        ba = str(b) + str(a)  
        if ab > ba: #a before b 
            return -1 
        elif ab < ba:  #b before a
            return 1
        else: #b equal a
            return 0

    res = sorted([str(i) for i in nums], key = cmp_to_key(compare))

    return str(int(''.join(res)))

            
# Review / Evaulate 
# n is length of numbers
# O(n log n) time for sorting 
# O(n) space for sorting in python and storing the result array



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - what if there are no answers?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# answers[i] equals to total number of rabbits seen besides current rabbit, increment result counter by (answers[i] + 1) for potential future rabbits seen. 
# everytime this current number of rabbits has been seen, decrement the current counter for answers[i]. If this count reaches 0, delete from dict. 
# Idea: A color recorded can only be recorded answers[i] times -> rabbit can say same number answers[i] times. 
# keep track of this number and add to result (answers[i] + 1) everytime when answers[i] is encountered more than answers[i] amount of times.


# Implement
# Translate the pseudocode into Python and share your final answer: 
def numRabbits(answers) -> int:
    seen = {}
    cnt = 0
    for i in answers: 
        if i == 0:
            cnt += 1
            continue
        if i not in seen:
            seen[i] = [i, i]
            cnt += (i + 1) 
        else: 
            seen[i][1] -= 1
            if seen[i][1] == 0:
                del seen[i] 
    return cnt
                  

# Review / Evaulate
# n is number of answers
# O(n) b/c looping through answers array, each operation within the loop is O(1)
# O(n) because storing previous seen answers worst case stores every answer. 