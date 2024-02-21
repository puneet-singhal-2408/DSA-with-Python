"""
Learn to check if number is an armstrong number

Problem Statement: Given a number, check if it is Armstrong Number or Not.

Example 1:
Input:153
Output: Yes, it is an Armstrong Number
Explanation: 1^3 + 5^3 + 3^3 = 153

Input:170
Output: No, it is not an Armstrong Number
Explanation: 1^3 + 7^3 + 0^3 != 170

Hint: Armstrong numbers:
numbers having the sum of digits raised to power no. of digits is equal to a given number.
Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers.

"""


def is_armstrong(number):
    """
        function to check armstrong number
    Args:
        number (): given number

    Returns:
        returns True if number is an Armstrong else False
    """
    # save original number
    original_number = number
    # get number of digits
    count = 0
    temp = number
    while temp != 0:
        count += 1
        temp //= 10
    # get sum of numbers power to count.
    sum_of_power = 0
    while number != 0:
        digit = number % 10
        sum_of_power += pow(digit, count)
        number //= 10
    return sum_of_power == original_number


if __name__ == '__main__':
    print(is_armstrong(153))
