"""
source: https://leetcode.com/problems/palindrome-number/


"""


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        result = str(x) == str(x)[::-1]
        print(result)
        return result


class Solution:
    """
    Approach 1: Revert half of the number

    >>> 1234 % 10
    4
    >>> 1234 // 10
    123
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False

        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x = x // 10

        return x == reversed_number or x == reversed_number // 10


if __name__ == '__main__':
    assert Solution().isPalindrome(112) is False
    assert Solution().isPalindrome(121) is True
