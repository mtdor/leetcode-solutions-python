"""
Class	Search algorithm
Data structure	Array
Worst-case performance	O(log n)
Best-case performance	O(1)
Average performance	O(log n)
Worst-case space complexity	O(1)

https://en.wikipedia.org/wiki/Binary_search_algorithm
https://www.geeksforgeeks.org/binary-search/
"""

from typing import Optional


def binary_search(
        data: list,
        target_value: int,
) -> Optional[int]:
    """
    Return index of 'target_value' in 'data' if it present there, else return None
    """
    left_index = 0
    right_index = len(data) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = data[mid_index]
        # return current index
        if target_value == mid_value:
            return mid_index
        # move to the right side
        elif target_value > mid_value:
            left_index = mid_index + 1
        # move to the left side
        else:
            right_index = mid_index - 1
    return None


def binary_search_recursion(
        data: list,
        target_value: int,
        left_index: int = 0,
        right_index: Optional[int] = None,
) -> Optional[int]:
    """
    Returns index of 'target_value' in 'data' if present, else None
    """
    # left_index = 0
    # if left_index is None:
    #     left_index = 0
    if right_index is None:
        right_index = len(data) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = data[mid_index]
        # return current index
        if target_value == mid_value:
            return mid_index
        # move to the right side
        elif target_value > mid_value:
            left_index = mid_index + 1
        # move to the left side
        else:
            right_index = mid_index - 1
    return None


def simple_binary_search() -> Optional[int]:
    # input data
    data = [2, 4]
    target_value = 4
    # main logic
    left_index = 0
    right_index = len(data) - 1  # 1

    # first iteration
    mid_index = (left_index + right_index) // 2  # 0
    mid_value = data[mid_index]  # 2
    # return current index
    if target_value == mid_value:  # (4 == 2) is False
        return mid_index
    # move to right side
    elif target_value > mid_value:  # (4 > 2) is True
        left_index = mid_index + 1  # 1
    # move to left side
    else:
        right_index = mid_index - 1

    # second iteration
    left_index = 1
    right_index = len(data) - 1  # 1

    mid_index = (left_index + right_index) // 2  # 1
    mid_value = data[mid_index]  # 4
    # return current index
    if target_value == mid_value:  # (4 == 2) is False
        return mid_index

    return None


if __name__ == '__main__':
    # input_list = [1, 2, 4, 7, 13, 22, 27, 35]
    input_list = [2, 4]
    target_value = 2

    result = binary_search(
        data=input_list,
        target_value=target_value,
    )
    # result = simple_binary_search()
    print('result:', result)
