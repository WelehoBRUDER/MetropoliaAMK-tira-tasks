def binary_search_iterative(array, value):
    """
    Performs a binary search in the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if array[mid] == value:
            return mid
        elif value < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None
