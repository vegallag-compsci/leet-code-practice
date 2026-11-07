"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in 
any order, but there's a constraint: there has to be a gap of at least n intervals between two 
tasks with the same label. Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two intervals before doing A again. The same applies 
to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, 
you can do A again as 2 intervals have passed.
"""

from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Two identical tasks must be (n+1) slots apart
        # 'counts' -> dict[task : frequency]
        # 'maxHeap' -> list[negative(frequency)]
        counts = Counter(tasks) # Counter({'A': 4, 'B': 1, 'C': 1})
        maxHeap = [-c for c in counts.values()] # [-4, -1, -1]

        # Rearrange into valid heap (parent <= children)
        heapq.heapify(maxHeap)

        # Queue of tasks that ran recently (can't run yet)
        # Each entry (timeWhenReady, negativeRemainingCount)
        cooldown = deque()

        # CPU clock (start at 0, increment by 1 every interval)
        time = 0

        # Keep going while any task is ready (heap) OR waiting to cool down (queue)
        # Stop only when both are empty (meaning every task has finished)
        while maxHeap or cooldown:
            # New interval begins (CPU Clock + 1)
            time += 1

            # If atleast one task is ready, run one now
            # If heap is empty, skip this and CPU idles this tick
            if maxHeap:
                # Take the task with the most copies left out of the heap
                # Running it uses up one copy (-3 -> -2), add 1
                remaining = 1 + heapq.heappop(maxHeap)

                # If remaining is 0, this task is completely done, so forget it
                # If not 0, it still has copies left, must cooldown first
                if remaining != 0:
                    # Ran at 'time', so it needs 'n' empty intervals after this one
                    # It can return to the heap at the end of tick (time + n)
                    # Store when it returns and how many copies remain
                    cooldown.append((time + n, remaining))
            
            # Check whether the task at the FRONT of queue has finished cooling
            # Front = the one that entered earliest, always the first to be ready
            # 'if' not 'while', only one task runs per tick
            # At most one task can finish cooling per tick
            # cooldown[0][0] = (timeWhenReady, ...)
            # If cooldown[0][0] == time, it's finished cooling
            if cooldown and cooldown[0][0] == time:
                # Remove it from queue (popleft) and grab its remaining count ([1])
                # Put it back in heap so it can be run on next tick
                heapq.heappush(maxHeap, cooldown.popleft()[1]) # .popleft()[1] -> negativeRemainingCount

        # Clock = Total Intervals used, Idles included
        return time

        
sol = Solution()
result = sol.leastInterval(["A", "A", "A", "A", "B", "C"], n = 2)
print("Result:", result)