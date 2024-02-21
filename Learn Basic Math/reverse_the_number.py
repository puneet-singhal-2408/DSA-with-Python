"""
Learn to reverse a number

Problem Statement: Given a number N reverse the number and print it.

Example 1:
Input: N = 123
Output: 321
Explanation: The reverse of 123 is 321

Example 2:
Input: N = 234
Output: 432
Explanation: The reverse of 234 is 432

Hint: Divide the number and save the remainder after each iteration concatenate previous remainder
with new remainder

"""


def reverse_number(number):
    """
        function to reverse a given number
    Args:
        number (): number to be reversed

    Returns:
        reverse of the given number
    """
    # initialize a variable to store the reversed number
    reverse = 0
    while number != 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    return int(reverse)


if __name__ == '__main__':
    print(reverse_number(123456))
