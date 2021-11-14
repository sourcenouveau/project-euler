"""
Project Euler: Problem 2
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four
million, find the sum of the even-valued terms.
"""

import argparse


def sum_even_fibonacci(limit: int) -> int:
    """
    Sums even terms in the Fibonacci sequence.
    :param limit: Limit for the sequence, non-inclusive.
    :return: Sum of even terms in the Fibonacci sequence.
    """
    term_a = 1
    term_b = 2
    result = 0

    while term_b < limit:
        if not term_b % 2:
            result += term_b

        term_a, term_b = term_b, term_a + term_b

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sum even terms in the Fibonacci sequence."
    )
    parser.add_argument("limit", type=int)

    args = parser.parse_args()

    result = sum_even_fibonacci(args.limit)

    print(f"Sum of even terms in the Fibonacci sequence below {args.limit}:")
    print(result)
