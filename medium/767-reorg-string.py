"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
 
Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""
"""

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
         # s = "xxxrwppk"
         # Create Dictionary of {char: count}
         count = Counter(s) # {'x':3, 'p':2, 'r':1, 'w':1, 'k':1}

         # List Comprehension to get maxHeap (heapq only has minHeaps, store count as negative)
         maxHeap = [[-cnt, char] for char, cnt in count.items()]

         # Rearrange into valid Heap order (parent <= children)
         heapq.heapify(maxHeap)

         # 'Prev' is the benched character, one we just used, cant be used next
         # 'Res' is the answer being built
         prev = None
         res = ""

         # Loop While -> Heap has characters   OR   something is benched in 'prev'
         while maxHeap or prev:
              # Failure Check (ex: "aaab" ends up with 2 a's adjacent -> Impossible, return)
              # Something is benched, but nothing else available to put between it and itself.
              if prev and not maxHeap:
                   return ""

              # Removes and returns top item (most freq element)
              # Since 'prev' out of heap, can't reuse char just used. Is how "Most Freq, Except Prev" is enforced.
              cnt, char = heapq.heappop(maxHeap)

              # Add the character to 'res' var to build answer
              # Increment count since they're negative (-3 -> -2), indicating 1 fewer char remaining
              res += char
              cnt += 1

              # Previously benched char has now sat out 1 iteration\
              # It is now safe to put back in heap
              if prev:
                   heapq.heappush(maxHeap, prev)
                   prev = None
              
              # If the char we just used still has copies left, bench it for next round
              # Alternatively, if 'cnt == 0', it's finished and gets discarded
              if cnt != 0:
                   prev = [cnt, char]

         return res
        
sol = Solution()
result = sol.reorganizeString("xxxrwppk")
print("Result:", result)