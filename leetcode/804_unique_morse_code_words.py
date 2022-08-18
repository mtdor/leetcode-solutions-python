from typing import List

MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
         "....", "..", ".---", "-.-", ".-..", "--", "-.",
         "---", ".--.", "--.-", ".-.", "...", "-", "..-",
         "...-", ".--", "-..-", "-.--", "--.."]


def char_to_morse(char):
    return MORSE[ord(char) - ord("a")]


def word_to_morse(word):
    return "".join([char_to_morse(char) for char in word])


def words_to_morse(words: List[str]) -> List[str]:
    return [word_to_morse(word) for word in words]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(words_to_morse(words)))


if __name__ == '__main__':
    assert Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2

    # print(char_to_morse("c"))
    # print(word_to_morse("cab"))
    # print(words_to_morse(["cab", "ab"]))
