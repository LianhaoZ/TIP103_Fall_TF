# PROBLEM 1
# Understand
# Share 2 questions you would ask to help understand the question:
# - can I use a greedy approach?
# - can the array be empty?

# Plan
# Write out in plain English what you want to do: 
# I will first get the count of all tasks to schedule. Then I wil use a maxheap to calcualte the time needed to schedule each
# tasks n apart, which also implies each cycle will take maximum of n tasks. I will first put all the frequencies into pq
# Then, while I can add more tasks to the cycle, I will pop from freq and store the value - 1, which I will put back into the pq after cycle is done.
# At each iteration, I will add the time taken for each cycle. If there are still tasks left then each cycle will take n+1 
# but if the pq is empty then how ever many tasks were scheduled during last iteration will be added. 

# Implement
# Translate the pseudocode into Python and share your final answer: 
def leastInterval(tasks, n):
    freq = [0] * 26
    for ch in tasks:
        freq[ord(ch) - ord('A')] += 1
        
    pq = [-f for f in freq if f > 0]
    heapq.heapify(pq)

    time = 0 
    while pq:
        cycle = n + 1
        store = []
        task_count = 0 
        while cycle > 0 and pq:
            current_freq = -heapq.heappop(pq)
            if current_freq > 1:
                store.append(-(current_freq - 1))
            task_count += 1
            cycle -= 1 
        for x in store:
            heapq.heappush(pq, x) 
        time += task_count if not pq else n + 1
    return time


# PROBLEM 2
# Understand
# Share 2 questions you would ask to help understand the question:
# - How can a vertial edge be represented?
# - Are there any additional space constraints?

# Plan
# Write out in plain English what you want to do: 
# I will create a dictionary to record the gaps (when a brick ends) in each level of the wall. 
# Then I will loop through the dictionary to find the gap that occurs the most frequent. 
# The minimum number of crossed bricks will then be length of bricked wall - the count of the gap that occurs the most freqent

# Implement
# Translate the pseudocode into Python and share your final answer: 
def leastBricks(wall):
    if not wall:
        return 0 
    leng = sum(wall[0]) 
    check = {}
    for i in wall:   
        ptr = 0
        for j in i:   
            ptr += j
            check[ptr] = check.get(ptr, 0) + 1 

    m = 0
    for i in check:
        if i == leng: 
            continue
        m = max(check[i], m)

    return len(wall) - m