def sum_first_n_numbers(n):
    if n == 1:
        return n
    return n + sum_first_n_numbers(n-1)


print(sum_first_n_numbers(10))
