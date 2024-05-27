def reverse_array(list_to_reverse):
    if len(list_to_reverse) == 0 or len(list_to_reverse) == 1:
        return list_to_reverse
    return list_to_reverse[-1:] + reverse_array(list_to_reverse[:len(list_to_reverse) - 1])


print(reverse_array([1, 2, 3, 4, 5, 7, 10, 55]))
