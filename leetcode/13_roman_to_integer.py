"""
source: https://leetcode.com/problems/roman-to-integer/

exclusions:
IV - 4
IX - 9
XL - 40
XC - 90
CD = 400
CM = 900
"""

ROMAN_TO_INT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution1:
    def romanToInt(self, s: str) -> int:
        result = 0
        prev_char = None
        for char in reversed(s):
            if prev_char and ROMAN_TO_INT[char] < ROMAN_TO_INT[prev_char]:
                result -= ROMAN_TO_INT[char]
            else:
                result += ROMAN_TO_INT[char]
            prev_char = char
        return result


class Solution2:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        return sum([ROMAN_TO_INT[ch] for ch in s])


Solution = Solution2

if __name__ == '__main__':
    assert Solution().romanToInt("I") == 1
    assert Solution().romanToInt("II") == 2
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("V") == 5
    assert Solution().romanToInt("VI") == 6
    assert Solution().romanToInt("X") == 10
    assert Solution().romanToInt("XX") == 20
    assert Solution().romanToInt("MMMDCCXXIV") == 3724
