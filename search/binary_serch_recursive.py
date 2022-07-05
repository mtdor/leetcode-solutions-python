"""
https://stackoverflow.com/questions/19989910/recursion-binary-search-in-python?answertab=trending#tab-top
"""
from typing import List

NONE_VALUE = -1


def binary_search(nums: List[int],
                  target: int) -> int:
    if not nums:
        return NONE_VALUE
    middle_index = len(nums) // 2
    middle_value = nums[middle_index]

    if target == middle_value:
        return middle_index
    elif len(nums) == 1:
        return middle_index if target == middle_value else NONE_VALUE
    elif target < middle_value:
        return binary_search(nums=nums[:middle_index], target=target)
    else:
        res = binary_search(nums=nums[middle_index + 1:], target=target)
        return middle_index + res + 1 if res != NONE_VALUE else NONE_VALUE


if __name__ == '__main__':
    result = binary_search(nums=[5], target=5)
    assert result == 0, result
    result = binary_search(nums=[15], target=5)
    assert result == 0, result
    result = binary_search(nums=[3], target=5)
    assert result == 1, result
    result = binary_search(nums=[1, 3, 5, 6, 9, 15, 21], target=5)
    assert result == 2, result
    result = binary_search(nums=[1, 3, 5], target=4)
    assert result == 2, result
    result = binary_search(nums=[1, 3, 5], target=6)
    assert result == 3, result
    result = binary_search(nums=[1, 3, 5, 6], target=5)
    assert result == 2, result
    result = binary_search(nums=[], target=4)
    assert result == NONE_VALUE, result
    result = binary_search(nums=[1, 3], target=4)
    assert result == NONE_VALUE, result
