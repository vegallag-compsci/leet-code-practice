"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1, 2, 3], the following are all the permutations of arr: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

Examples:
The next permutation of arr = [1, 2, 3] is [1, 3, 2].
The next permutation of arr = [2, 3, 1] is [3, 1, 2].
The next permutation of arr = [3, 2, 1] is [1, 2, 3] because [3, 2, 1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
"""

from collections import Counter

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Dont return anything; modify in place
        # (i, v) -> (index, value)
        # x[0] -> index, x[1] -> value
        prev = None
        toSwap = None
        swapper = None

        # Read right to left, find # not decreasing
        for i,v in enumerate(nums[::-1]):
            if prev and prev[1] > v:
                toSwap = (i, v)
                print(f"{v} < {prev[1]} (toSwap={toSwap})")
                for x,y in enumerate(nums[::-1]):
                    if y > v:
                        swapper = (x, y)
                        break
                break
            else:
                prev = (i, v)

        print(f"(toSwap={toSwap}), (swapper={swapper})")
        
        # If no # is found in loop, array is already largest permutation
        # Simply reverse list and return it
        if toSwap == None:
            nums.reverse()
            return

        # Swap the 2 pivots in place
        nums[((len(nums))-1) - toSwap[0]] = swapper[1]
        nums[((len(nums))-1) - swapper[0]] = toSwap[1]

        # Reverse the remaining tail
        left = (len(nums) - 1 - toSwap[0]) + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Return modified list
        print(f"Nums: {nums}")


sol = Solution()
result = sol.nextPermutation(nums=[1,3,5,4,2])
# print("Result:", result)