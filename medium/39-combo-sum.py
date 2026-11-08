"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique 
combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 
combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

from collections import Counter

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Given (candidates = [2, 3, 5]) (target = 8)
        # Expected -> [[2,2,2,2],[2,3,3],[3,5]]

        # Helper function to explore all valid combos
        # (start_index) -> current index in 'candidates' to avoid duplicates
        # (remaining_sum) -> remaining sum needed to reach target
        def backtrack(start_index: int, remaining_sum: int) -> None:
            # Base case (valid combo)
            if remaining_sum == 0:
                result.append(current[:])
                return
            
            # Pruning (if remaining sum < smallest avail candidate)
            if remaining_sum < candidates[start_index]:
                return

            # Try each candidate from start_index onward
            for i in range(start_index, len(candidates)):
                # Include the current candidate
                current.append(candidates[i])

                # Recursively explore w/ same index (allowing reuse)
                backtrack(i, remaining_sum - candidates[i])

                # Backtrack: remove the last added candidate
                current.pop()

        # Sort candidates for optimization
        candidates.sort()

        # Initialize variables
        current = [] # -> Current combo being built
        result = [] # -> All valid combo's found

        # Call helper (backtracking process)
        backtrack(0, target)

        # Return 'result' of all final combo's
        return result


sol = Solution()
result = sol.combinationSum(candidates = [2,3,5], target = 8) # -> [[2,2,2,2],[2,3,3],[3,5]]
print("Result:", result)