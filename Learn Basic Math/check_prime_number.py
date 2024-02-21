"""
Learn how to check a prime number

Problem Statement: Given a number, check whether it is prime or not.
A prime number is a natural number that is only divisible by 1 and by itself.

Example 1:
Input: N = 3
Output: Prime
Explanation: 3 is a prime number

Example 2:
Input: N = 26
Output: Non-Prime
Explanation: 26 is not prime

"""


# Approach 1: iterating all number from 2 to N
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# Approach 2: Optimal approach:
# if it is divisible by divisor it will be divisible by its quotient too,
# so we do not need to run the loop till N, we can run it till sqrt of given number.
def check_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(check_prime(3))
    print(is_prime(26))
