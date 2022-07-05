
PARENTHESES = {
    "(": ")",
    "[": "]",
    "{": "}",
}


class Solution:
    def isValid(self, s: str) -> bool:
        close_chars_expected = []
        for char in s:
            # handle open char
            if char in PARENTHESES.keys():
                close_char = PARENTHESES[char]
                close_chars_expected.append(close_char)
            # handle close char
            else:
                try:
                    close_char_expected = close_chars_expected.pop()
                except IndexError:
                    return False
                if close_char_expected != char:
                    return False
        if close_chars_expected:
            return False
        return True


if __name__ == '__main__':
    # assert Solution().isValid("()") is True
    # assert Solution().isValid("[]") is True
    # assert Solution().isValid("{}") is True
    # assert Solution().isValid("()(]") is False
    # assert Solution().isValid("]") is False
    assert Solution().isValid("[") is False
    # assert Solution().isValid("{[]}") is True
