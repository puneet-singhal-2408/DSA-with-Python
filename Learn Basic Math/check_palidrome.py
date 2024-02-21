"""
learn to check if a string/number is a palindrome

Problem Statement:  Given a number check if it is a palindrome.

Example 1:
Input: N = 123
Output: Not Palindrome Number
Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

Example 2:
Input: N =  121
Output: Palindrome Number
Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.

Hints: An integer is considered a palindrome when it reads the same backward as forward.

"""


def check_palindrome(number: int) -> bool:
    """
        function to check whether a number is a palindrome
    Args:
        number (): number to be checked

    Returns:
        return True if number is palindrome else False
    """
    # we will update the given number so we are saving original number to compare.
    original_number = number
    # variable to save reverse of a number
    reverse = 0
    # reversing the given number.
    while number != 0:
        reverse = reverse * 10 + number % 10
        number = number // 10
    # return True if number is palindrome else False
    return original_number == reverse


if __name__ == '__main__':
    print(check_palindrome(121))

