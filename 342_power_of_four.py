"""
https://leetcode.com/problems/power-of-four/
https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2
https://www.geeksforgeeks.org/find-whether-a-given-number-is-a-power-of-4-or-not/#:~:text=Take%20log%20of%20given%20number,power%20of%204%2C%20else%20not.
"""


# Time Complexity: O(log4n)
# Auxiliary Space: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 4 != 0:
                return False
            n = n // 4
        return True


if __name__ == '__main__':
    assert Solution().isPowerOfFour(-1) is False
    assert Solution().isPowerOfFour(0) is False
    assert Solution().isPowerOfFour(5) is False
    assert Solution().isPowerOfFour(1) is True
    assert Solution().isPowerOfFour(16) is True
    assert Solution().isPowerOfFour(8) is False
