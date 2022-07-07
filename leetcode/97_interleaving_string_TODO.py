"""
https://leetcode.com/problems/interleaving-string/
"""


# TODO: unsolved
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_counter = 0
        s2_counter = 0

        for char in s3:
            if s1[s1_counter] == char:
                s1_counter += 1
            elif s2[s2_counter] == char:
                s2_counter += 1
            else:
                return False

        return True


if __name__ == '__main__':
    # assert Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is True
    # assert Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc") is False
    assert Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac") is False
