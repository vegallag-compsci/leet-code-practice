"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Empty string case
        if not s:
            return ""

        # Initialize variables
        start = 0
        maxLength = 0

        # Helper func
        def expandFromCenter(left: int, right:int) -> int:
            # Expand outward if bounds are valid & chars match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of palindrome ('- 1' accounts for extra steps)
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindrome
            len1 = expandFromCenter(i, i)
            # Even length palindrome
            len2 = expandFromCenter(i, i+1)
            # Find max of both expansions
            currMax = max(len1, len2)
            # If longer than previous best, update start pointer
            if currMax > maxLength:
                maxLength = currMax
                # Calculate where palindrome starts
                start = i - (currMax - 1) // 2

        return s[start:start + maxLength]


sol = Solution()
result = sol.longestPalindrome(s = "babad")
print("Result:", result)