"""
Project Euler: Problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import argparse
import functools


@functools.cache
def is_prime(value: int) -> bool:
    """
    Determines whether the provided value is prime.
    :param value: Value to examine.
    :return: True if the value is prime, False otherwise.
    """
    return not any(value % x == 0 for x in range(2, value // 2))


def largest_prime_factor(value: int) -> int:
    """
    Finds the largest prime factor of the provided value.
    :param value: Value to factor.
    :return: The largest prime factor.
    """
    divider = 2
    result = value

    while divider < result:
        if value % divider == 0:
            factor = value // divider

            if is_prime(factor):
                result = factor

        divider += 1

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Finds the largest prime factor.")
    parser.add_argument("value", type=int)

    args = parser.parse_args()

    result = largest_prime_factor(args.value)

    print(f"Largest prime factor of {args.value}:")
    print(result)
