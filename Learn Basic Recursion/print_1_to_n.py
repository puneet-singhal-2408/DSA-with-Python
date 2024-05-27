def print_1_to_n(start, end):
    if start > end:
        return
    print(start)
    print_1_to_n(start + 1, end)


print_1_to_n(1, 10)
