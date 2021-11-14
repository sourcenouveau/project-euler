"""
Project Euler: Problem 1
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import argparse


def find_sum_of_multiples_of_3_and_5(limit: int) -> int:
    """
    Finds the sum of all multiples of 3 and 5 below the provided limit.
    :param limit: Limit for multiples to search, non-inclusive.
    :return: Sum of all multiples.
    """
    # Sum the multiples of 3 and 5, but subtract the multiples of 15 which get counted
    # twice.
    return sum(range(0, limit, 3)) + sum(range(0, limit, 5)) - sum(range(0, limit, 15))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("limit", type=int, help="search limit")

    args = parser.parse_args()

    result = find_sum_of_multiples_of_3_and_5(args.limit)

    print(f"Sum of multiples of 3 and 5 below {args.limit}:")
    print(result)
