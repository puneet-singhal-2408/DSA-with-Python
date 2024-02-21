"""
learn to get the highest common factor or greatest common divisor

Problem Statement: Find the gcd of two numbers.

Example 1:
Input: num1 = 4, num2 = 8
Output: 4
Explanation: Since 4 is the greatest number which divides both num1 and num2.

Example 2:
Input: num1 = 3, num2 = 6
Output: 3
Explanation: Since 3 is the greatest number which divides both num1 and num2.

Hint: GCD/HCF cannot become greater than the smallest number.
"""


# Approach 1: Also known as Brute force approach

def greatest_common_divisor(num1, num2):
    """
        function to get the greatest common divisor of two numbers
    Args:
        num1 (): first number
        num2 (): second number

    Returns:
        greatest common divisor
    """
    # smallest gcd for any two number is 1, so will start from 1
    gcd = 1
    # iterate till the smallest number in given numbers
    for i in range(1, min(num1, num2) + 1):
        # check if I divide both number
        if num1 % i == 0 and num2 % i == 0:
            # store the number which divides both.
            gcd = i
    return gcd


# Approach 2: Optimal approach using recursion.

def highest_common_divisor(num1, num2):
    """
        function to get the highest common divisor of two numbers
        Args:
            num1 (): first number
            num2 (): second number

        Returns:
            highest common divisor
        """
    # base condition
    # HCF among two numbers will be other number if any of the number is zero
    if num2 == 0:
        return num1
    return highest_common_divisor(num2, num1 % num2)


if __name__ == "__main__":
    print(greatest_common_divisor(4, 8))
    print(highest_common_divisor(3, 6))
    print(highest_common_divisor(0, 6))
