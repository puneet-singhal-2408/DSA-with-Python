"""
Learn to count the number of digits in a given number.

Problem Statement: Given an integer N, write a program to count the number of digits in N.

Example 1:
Input: N = 12345
Output: 5
Explanation: N has 5 digits

Example 2:
Input: N = 8394
Output: 4
Explanation: N has 4 digits

Hint: when you divide a number by 10 remainder is its last digit and quotient is remaining number
"""


def count_digits(number):
    """
        function to return the number of digits in a given number
    Args:
        number (): number to be counted digits.
    Returns:
        int: number of digits in a given number
    """
    # create a variable to count digits
    count = 0
    # we will do floor division of number with 10 until we get quotient as 0
    while number != 0:
        # divide the number by 10 and assign the quotient back to number
        number //= 10
        # increase the count for each iteration till number become 0
        count += 1

    return count


if __name__ == '__main__':
    print(count_digits(12345))
