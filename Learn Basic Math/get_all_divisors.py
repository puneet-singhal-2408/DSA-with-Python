"""
Learn to find all divisors of a number

Problem Statement: Given a number, print all the divisors of the number.
A divisor is a number that gives the remainder as zero when divided.

Example 1:
Input: n = 36
Output: 1 2 3 4 6 9 12 18 36
Explanation: All the divisors of 36 are printed.

Example 2:
Input: n = 97
Output: 1 97
Explanation: Since 97 is a prime number, only 1 and 97 are printed.

Hint: we will see only optimal approach for this.
1----------->36
2----------->18
3----------->12
4----------->9
6----------->6
In optimal approach the output is unordered.

"""


def get_all_divisors(number):
    # iterate from 1 to square root of given number, in case odd we will add 1 to square root.
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            print(i, end=" ")
            # in case of perfect square divisor is equal to quotient, so we will ignore it.
            if i != number / i:
                print(int(number / i), end=" ")


if __name__ == "__main__":
    get_all_divisors(36)
