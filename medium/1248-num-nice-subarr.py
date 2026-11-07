"""
Given an array of integers nums and an integer k. A continuous 
subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
"""

from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        # Store frequency of each prefix sum value
        count = Counter({0: 1})
        ans = 0     # Final count
        t = 0       # Running count of odd #'s

        # Traverse 'nums' array
        for v in nums:
            # Update odd count ('t')
            # (1 & 1) = 1, since 1 is odd, t = 1
            t += (v & 1)

            # Count valid subarrays
            # Check count[t - k]
            # count[1 - 3] = count[-2] = 0, ans += 0
            ans += count[t - k]

            # Update counter (count[t])
            # count[1] += 1 -> {0: 1, 1: 1}
            count[t] += 1

        # Return the finalized count
        return ans

sol = Solution()
result = sol.numberOfSubarrays(nums = [1, 1, 2, 1, 1], k = 3)
print("Result:", result)