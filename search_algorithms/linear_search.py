"""
Linear search is sequential search of the list.
that scans the list from the beginning till the required value is found.
or the list is exhausted.
"""


def linear_search(lst, value):
    """
        function to check if the list have required value
    Args:
        lst (): list of numbers
        value (): value to be searched

    Returns:
        returns true if the value is found, false otherwise
    """
    # iterate on each value
    for i in lst:
        # return true value in list
        if i == value:
            return True
    return False


if __name__ == "__main__":
    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(linear_search(num_lst, 8))
