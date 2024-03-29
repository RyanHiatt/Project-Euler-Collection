import math
import numpy as np
import itertools

#######################################
# Project Euler Mathematical Problems
# Problems 1 - 20
# Accomplished by: Ryan Hiatt
# Start Date: 10/12/2021
# Completion Date: TBD
#######################################

# region Problem 1 - Multiples of 3 or 5
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(n1, n2, limit):
    return sum([i if i % n1 == 0 or i % n2 == 0 else 0 for i in range(limit)])


# print(f"Answer 1 = {sum_of_multiples(n1=3, n2=5, limit=1000)}")

# endregion


# region Problem 2 - Even Fibonacci Numbers
""" Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


# Create a fibonacci sequence from two starting values and a limit
def fibonacci_sequence(n1, n2, limit):
    fib_seq = [n1, n2]
    while True:
        if fib_seq[-1] + fib_seq[-2] <= limit:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        else:
            return fib_seq


def even_fibonacci_sequence(n1, n2, limit):
    for element in fibonacci_sequence(n1=n1, n2=n2, limit=limit):
        if element % 2 == 0:
            yield element


# print(f"Answer 2 = {sum(list(even_fibonacci_sequence(n1=1, n2=2, limit=4000000)))}")

# endregion


# region Problem 3 - Largest Prime Factor
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_prime_factors(number):
    while number % 2 == 0:
        yield 2
        number /= 2

    for i in range(3, int(math.sqrt(number) + 1), 2):
        while number % i == 0:
            yield i
            number /= i

    if number > 2:
        yield number


# print(f"Answer 3 = {max(list(get_prime_factors(600851475143)))}")

# endregion


# region Problem 4 - Largest Palindrome Product
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_product(start, stop):
    i_values = (i for i in range(start, stop + 1))
    palindromes = []
    for i in i_values:
        j_values = (i for i in range(start, stop + 1))
        for j in j_values:
            if str(i * j) == str(i * j)[::-1]:
                palindromes.append(i * j)
    return max(palindromes)


# print(f"Answer 4 = {largest_palindrome_product(100, 999)}")

# endregion


# region Problem 5 - Smallest Multiple
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def smallest_multiple(min_val, max_val):
    numbers = np.arange(start=min_val, stop=max_val + 1)
    multiple = np.array([max_val] * max_val)

    while True:
        if np.all(multiple % numbers == 0):
            return multiple[0]
        else:
            multiple += max_val


# print(f"Answer 5 = {smallest_multiple(min_val=1, max_val=20)}")

# endregion


# region Problem 6 - Sum Square Difference
"""
The sum of the squares of the first ten natural numbers is:
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:
    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square_difference(n):
    sum_of_square = 0
    for i in range(n + 1):
        sum_of_square += i * i

    square_of_sum = sum(range(n + 1)) ** 2

    return square_of_sum - sum_of_square


# print(f"Answer 6 = {sum_square_difference(n=100)}")

# endregion


# region Problem 7 - 10,001 Prime
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""


# def sieve_of_eratosthenes(limit):  # Generate prime numbers up to a limit
#     a = [True] * limit  # Initialize the primality list
#     a[0] = a[1] = False
#
#     for (i, isprime) in enumerate(a):
#         if isprime:
#             yield i
#             for n in range(i*i, limit, i):  # Mark factors non-prime
#                 a[n] = False


def generate_primes(n_primes):  # Generate prime numbers up to a limit
    primes = []
    n = 2
    while len(primes) < n_primes:
        if all(n % i for i in itertools.islice(itertools.count(2), int(math.sqrt(n) - 1))):
            primes.append(n)
        n += 1
    return primes


# print(f"Answer 7 = {generate_primes(n_primes=10001)[-1]}")

# endregion


# region Problem 8 - Largest Product in a Series
"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

number = """
7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843
8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557
6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749
3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776
6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397
5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474
8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586
1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408
0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606
0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
""".replace("\n", "")


def largest_adj_product(series, num_digits):
    # Segment possible pools of numbers that do not contain zero
    num_pool = series.split("0")
    largest_product_series = None
    largest_product_obj = 0

    # check if the length of the segmented number is too short
    for index, n in enumerate(num_pool):
        if len(n) >= num_digits:
            # iterate through each group of num_digits within n
            for i in range(len(n) - num_digits + 1):
                iter_series = []
                iter_obj = 1

                # calculate iteration series and objective
                for j in range(i, i + num_digits):
                    iter_series.append(n[j])
                    iter_obj *= int(n[j])

                if iter_obj > largest_product_obj:  # Update series and objective
                    largest_product_series = iter_series
                    largest_product_obj = iter_obj

    return largest_product_series, largest_product_obj


# s, p = largest_adj_product(series=number, num_digits=13)
# print(f"Answer 8 = Series: {s}, Product: {p}")

# endregion


# region Problem 9 - Special Pythagorean Triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet(goal):
    triplet_sum = 0
    m = 2
    n = 1

    while triplet_sum <= goal:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        triplet_sum = a + b + c

    return a, b, c


print(f"Answer 9 = {pythagorean_triplet(3, 1)}")

# endregion
