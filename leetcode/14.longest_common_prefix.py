"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if len(strs) == 0:
            return result
        pivot_word = strs[0]

        for i in range(len(pivot_word)):
            result += pivot_word[i]
            for item_word in strs[1:]:
                try:
                    if item_word[i] == pivot_word[i]:
                        pass
                    else:
                        print('result', result[:-1])
                        return result[:-1]
                except IndexError:
                    print('result', result[:-1])
                    return result[:-1]

        print('result', result)
        return result


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flight", "flow"]) == "fl"
    assert Solution().longestCommonPrefix(["flow", "flower"]) == "flow"
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
