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
        longest = ""
        if len(strs) == 0: 
            return longest
        elif len(strs) == 1:
            return strs[0]
        
        for i in range(len(strs[0])):
            # loops thru every char in first word
            char = strs[0][i]
            for z in range(len(strs)):
                # loops thru entire rest of list
                if i > len(strs[z]) - 1:
                    return longest
                if strs[z][i] == char:
                    if z == len(strs) - 1:
                        longest += char
                    continue
                else:
                    return longest
        return longest
            

sol = Solution()
test_strs = ["flower", "flow", "flowght"]


result = sol.longestCommonPrefix(test_strs)
print("Result:", result)
