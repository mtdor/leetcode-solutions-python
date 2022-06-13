"""
# Quick sort in Python
https://www.programiz.com/dsa/quick-sort

debug iterations:

data = [8, 7, 6, 1, 0, 9, 2]
pivot: 2 [1, 0, 2, 8, 7, 9, 6]
pivot: 0 [0, 1, 2, 8, 7, 9, 6]
pivot: 3 [0, 1, 2, 6, 7, 9, 8]
pivot: 5 [0, 1, 2, 6, 7, 8, 9]
"""


# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pivot = partition(array, low, high)
        print('pivot:', pivot, array)
        # [1, 0, 2, 8, 7, 9, 6]

        # recursive call on the left of pivot
        quick_sort(array, low, pivot - 1)

        # recursive call on the right of pivot
        quick_sort(array, pivot + 1, high)


if __name__ == '__main__':
    # data = [8, 7, 6, 1, 0, 9, 2]
    # data = [0, 1, 2, 8, 7, 9, 6]  # test
    data = [0, 1, 2, 6, 7, 9, 8]  # test
    # data = [1, 0, 2]  # test
    print("Unsorted Array", data)

    size = len(data)

    # quick_sort(data, 0, size - 1)
    # quick_sort(data, 0, 1)  # test
    quick_sort(data, 4, 6)  # test
    """
    pivot:1 3 [0, 1, 2, 6, 7, 9, 8]
    pivot:1 4 [0, 1, 2, 6, 8, 9, 7]
    pivot:1 5 [0, 1, 2, 6, 8, 7, 9]
    """

    print('Sorted Array in Ascending Order:', data)
