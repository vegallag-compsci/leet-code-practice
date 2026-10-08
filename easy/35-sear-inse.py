"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
 
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, number in enumerate(nums):
            if number == target:
                return i
            if number < target:
                if i+1 == len(nums):
                    return i+1
                elif nums[i+1] > target:
                    return i+1
            if number > target:
                return i


sol = Solution()
result = sol.searchInsert([1], 1)
print("Result:", result)