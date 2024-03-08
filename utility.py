"""
file: utility.py
author: put your name here
"""
import random

def eea(r0, r1):
    """
    Pre-condition ro > r1 >=0
    :param r0: integer
    :param r1: integer
    :return: (gcd(r0, r1), s, t), where gcd(r0, r1) = s*r0 + t*r1
    """
    return None

def inverse(a, m):
    """
    Returns the inverse of a mod m if it exists, or None otherwise.
    :param a: integer
    :param m: integer or None
    """
    return None
    
def get_prime(bits, s):
    """
    Uses Miller Rabin primality test to generate a prime.
    You may use the random.randint() function.
    Do not use any built-in functions for generating prime numbers.
    :param bits: number of bits in generated primes
    :param s: security parameter
    :return: a probable prime of the length of the specified bits
    """
    return None


def mod_pow(x, e, n):
    """
    Use the fast exponent algorithm we discussed in class.
    You are not allowed to use any built-in functions such as pow() 
    or any other algorithms we never discussed in class.
    :param x: base
    :param e: exponent
    :param n: modulus
    :return: x^e mod n
    """
    return None