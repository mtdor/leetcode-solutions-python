"""
source: https://leetcode.com/problems/roman-to-integer/


"""

ROMAN_TO_INT = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev_char = None
        for char in reversed(s):
            if prev_char and ROMAN_TO_INT[char] < ROMAN_TO_INT[prev_char]:
                result -= ROMAN_TO_INT[char]
            else:
                result += ROMAN_TO_INT[char]
            prev_char = char
        # print('result', result)
        return result


if __name__ == '__main__':
    # assert Solution().romanToInt("I") == 1
    # assert Solution().romanToInt("II") == 2
    # assert Solution().romanToInt("III") == 3
    # assert Solution().romanToInt("IV") == 4
    # assert Solution().romanToInt("V") == 5
    # assert Solution().romanToInt("VI") == 6
    # assert Solution().romanToInt("X") == 10
    # assert Solution().romanToInt("XX") == 20
    assert Solution().romanToInt("MMMDCCXXIV") == 3724
