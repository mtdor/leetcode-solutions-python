"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack)):
            char = haystack[i]
            for j in range(len(needle)):
                char_needle = needle[j]
                # if char_needle == char:
                #     if index == -1:
                #         index = i
                # else:
                #     index = -1

                if char_needle != char:
                    break
                if index == -1:
                    index = i
                # if char_needle == char and index == -1:
                #     index = i
                # if char_needle != char and index != -1:
                #     return -1
        print('index', index)
        return index


if __name__ == '__main__':
    # assert Solution().strStr(haystack="hello", needle="ll") == 2
    assert Solution().strStr(haystack="hello", needle="lo") == 3
