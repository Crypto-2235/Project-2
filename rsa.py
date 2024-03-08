"""
file name: rsa.py
author: put your name here
"""

import random
import utility
import sys

def key_generation(bits, s):
    """
    Use the utility functions you wrote to generate RSA keys
    :param bits: the number of bits in n
    :param s: security parameter
    :return: (n,e,d), where (n,e) is a public key and d is a private key
    """
    return None

def encrypt(x, e, n):
    """
    Use the mod_pow funciton to encrypt x
    :param x: plaintext
    :param e: public key
    :param n: publick key
    :return: x^e mod n
    """
    return None

def decrypt(y, d, n):
    """
    Use the mod_pow funciton to decrypt y
    :param y: ciphertext
    :param d: private key
    :param n: public key
    :return: y^d mod n
    """
    return None

def main():
    """
    Test RSA key generation, encrytion, and decryption.
    :return: None
    """
    bit_length = 1024  # 2048 bits may take a few seconds
    security_parameter = 5
    (n, e, d) = key_generation(bit_length, security_parameter)
    print("public key: (", n, ",", e, ")")
    print("private key:", d)
    x = int(sys.argv[1])
    print("x =", x)
    y = encrypt(x, e, n)
    print("y =", y)
    z = decrypt(y, d, n)
    print(z == x)

if __name__ == "__main__":
    main()

