"""
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Integer array 'nums', integer 'k'
        # Return the top 'k' most freq elements
        count = Counter(nums)

        topKeys = [key for key, _ in count.most_common(k)]
        print(f"(count: {count}), (topKeys: {topKeys})")

        return topKeys


sol = Solution()
result = sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2)
print("Result:", result)