"""
Binary search works on sorted list only.
In binary search we examine the middle value.
If it matches the required value we stop.
Else we have to search on left or right side of middle value.
Depending on whether the searched value is greater or lesser than middle value.

"""


"""
Steps:
1. check if list is sorted.
2. find mid value and check with required value
3. compare if value is greater or lesser.
4. based on above comparison check in left or right.
"""


def binary_search(lst, value):
    """
        function to search value in sorted list
    Args:
        lst (): list of numbers
        value (): number to be searched

    Returns:
        index of value in sorted list
    """
    # get lowest and highest value from the
    low, high = 0, len(lst) - 1
    while low <= high:
        # get index of mid value
        mid = int((low + high)/2)
        # if mid value is required value return
        if lst[mid] == value:
            return mid
        # move towards left in list
        elif lst[mid] < value:
            low = mid + 1
        # move towards right in list
        else:
            high = mid - 1
    return None


if __name__ == '__main__':
    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(num_lst, 7))
