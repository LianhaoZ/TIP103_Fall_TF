# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a heapq?
# - can the pings be at negative times?

# Plan
# Write out in plain English what you want to do: 
# I will maintain a minheap or priority queue(PQ), whenever a ping t comes in, 
# push to pq. while the minimum element is less than t-3000, 
# heappop. The len of pq will be the amount of pings that is not less than t-3000. 

# Implement
# Translate the pseudocode into Python and share your final answer: 
import heapq
class RecentCounter:
    def __init__(self): 
        self.req = []
        heapq.heapify(self.req)

    def ping(self, t: int) -> int:
        heapq.heappush(self.req, t)
        while self.req[0] < t - 3000:
            heapq.heappop(self.req)
        return len(self.req)

# Review / Evaulate 
# n is max size of self.req at a time
# O(nlogn) time for worse case having to pop every previous request 
# O(n) space, worse case we would store every request



# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - How can what if I pop when the stack is empty?
# - Are there any additional time constraints?

# Plan
# Write out in plain English what you want to do: 
# I will maintain 2 stacks. The first stack to keep track when a element is 
# added and the second to keep track when element is checked(i.e. peeked or pop).
# if I pop or peek and st2 is empty, then I will pop froms stack 1. For the empty(), 
# return true only if both stacks are empty.

# Implement
# Translate the pseudocode into Python and share your final answer: 
class MyQueue:

    def __init__(self):
        self.st1 = [] #from the back
        self.st2 = [] #forwards

    def push(self, x: int) -> None:
        self.st1.append(x) 

    def pop(self) -> int:
        if not self.st2: 
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop() 

    def peek(self) -> int:
        if not self.st2: 
            while self.st1:
                self.st2.append(self.st1.pop()) 
        return self.st2[-1]  
        
    def empty(self) -> bool:
        return not self.st1 and not self.st2

# Review / Evaulate
# n is size of elemnts pushed to queue
# O(1) for push and empty. O(n) worst case for peek and pop() in case all elements were in stack 1 and needs to be moved to stack 2.
# O(n) time for storing elements in the queue