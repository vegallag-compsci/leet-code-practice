"""
Given a string s, return the maximum number of occurrences 
of any substring under the following rules:

1. The number of unique characters in the substring must be less than or equal to maxLetters.
2. The substring size must be between minSize and maxSize inclusive.

Example 1:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 occurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
"""

from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # For each substring:
        # 1) number of unique chars must be <= maxLetters 
        #    (if max = 2, 'aa','ab','bb' valid, 'abc' not)
        # 2) size of substr must (minSize <= k <= maxSize)

        # Generate all substrings of length minSize
        subs = []
        for i in range(len(s) - minSize + 1):
            subs.append(s[i:i+minSize])
        print(subs)
        # For each substring, check if it has at most 'maxLetters' unique chars
        
        # Count the freq of valid substrings using a hash table

        # Return the max freq found
        return 1


sol = Solution()
result = sol.maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4)
print("Result:", result)