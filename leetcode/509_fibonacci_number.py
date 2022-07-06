"""
https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, n: int) -> int:
        if n in (0, 1):
            return n
        return Solution().fib(n - 1) + Solution().fib(n - 2)


if __name__ == '__main__':
    assert Solution().fib(0) == 0
    assert Solution().fib(1) == 1
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    assert Solution().fib(5) == 5
    assert Solution().fib(6) == 8
