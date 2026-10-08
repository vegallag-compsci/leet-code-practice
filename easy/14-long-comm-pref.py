"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
    """

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        x = ""
        y = 0
        for char in strs[0]:
            if char == strs[1][y] and char == strs[2][y]:
                x += char
            else:
                return x
            y += 1
            

sol = Solution()
test_strs = ["flower", "flow", "flowght"]


result = sol.longestCommonPrefix(test_strs)
print("Result:", result)
