def print_names(n_times, name):
    if n_times > 0:
        print(name)
        print_names(n_times - 1, name)


print_names(10, 'Recursion')
