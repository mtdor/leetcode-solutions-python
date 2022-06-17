"""
дан отсортированый массив чисел, и число K
нужно вернуть два числа, которорые в сумме дают заданое число K

примеры:
[-1, 2, 5, 8], K=7; result: [-1, 8]
[-3, -1, 0, 2, 6], K=6; result: [0, 6]
[2, 4, 5], K=8; result: []
[-2, -1, 1, 2], K=0; result: [-2, 2]
[-3, 2, 0, 4, 5], K=7; result: [2, 5]

links:
source: https://www.youtube.com/watch?v=JtMuXmmDl9s
https://wiki.python.org/moin/TimeComplexity


оптимизация:
добится сложности N
* один раз проходим по массиву
* пробовать вычетать
"""


def fn_2n(array, k):
    array_length = len(array)
    for i in range(array_length):
        for j in range(i + 1, array_length):
            if array[i] + array[j] == k:
                return [array[i], array[j]]
    return []


def fn_list_index(array, k):
    """
    solution via check element in array (index)
    время работы: O(n)
    память: O(1)
    """
    array_length = len(array)
    for i in range(array_length):
        item = array[i]
        expected_number = k - item
        try:
            # complexity O(n)
            if array.index(expected_number):
                return [array[i], expected_number]
        except ValueError:
            pass
        # TODO: Check operation "in"
        # if expected_number in array:

    return []


def fn_via_set(array, k):
    """
    solution via check element in array (index)
    время работы: O(n)
    память: O(n)
    """
    tmp_set = set()
    for item in array:
        expected_number = k - item
        if expected_number in tmp_set:
            return [item, expected_number]
        else:
            tmp_set.add(item)
    return []


main = fn_via_set

if __name__ == '__main__':
    # print(main([-1, 2, 5, 8], 7))
    # print(main([-3, -1, 0, 2, 6], 6))
    # print(main([2, 4, 5], 8))
    # print(main([-2, -1, 1, 2], 0))
    print(main([-3, 2, 0, 4, 5], 6))
