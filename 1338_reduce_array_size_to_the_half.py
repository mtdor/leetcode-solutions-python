"""
https://leetcode.com/problems/reduce-array-size-to-the-half/

solution:
https://leetcode.com/problems/reduce-array-size-to-the-half/discuss/1319416/C%2B%2BJavaPython-HashMap-and-Sort-then-Counting-Sort-O(N)-Clean-and-Concise

algorithm:
1. count the frequency of each number
2. sort `frequencies` by ascending order



"""
from collections import Counter
from typing import List, Dict


def count_frequency(data: List[int]) -> Dict[int, int]:
    result = {}
    for item in data:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = count_frequency(arr)
        # print(freq)
        # {3: 4, 5: 3, 2: 2, 7: 1}
        frequencies = list(freq.values())
        frequencies.sort()
        print(frequencies)
        # [1, 2, 3, 4]

        unique_el, elements, mid = 0, 0, len(arr) // 2
        print(unique_el, elements, mid)
        # 0 0 5
        while elements < mid:
            unique_el += 1
            elements += frequencies.pop()
        return unique_el


if __name__ == '__main__':
    assert Solution().minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
