"""
Selection Sort Algorithm

Time Complexity
Best	O(n2)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	No
https://www.programiz.com/dsa/selection-sort - illustrated example
https://stackoverflow.com/questions/36700830/selection-sort-algorithm - representative picture
"""


def swap_elements(collection, i, j):
    collection[i], collection[j] = collection[j], collection[i]


def selection_sort(collection):
    size = len(collection)
    for i in range(size):
        min_idx = i
        for j in range((i + 1), size):
            if collection[j] < collection[min_idx]:
                min_idx = j
        if i == min_idx:
            continue
        swap_elements(collection, i, min_idx)


if __name__ == '__main__':
    print('selection_sort')
    input_collection = [20, 12, 10, 15, 2]
    selection_sort(input_collection)
    print('result', input_collection)
