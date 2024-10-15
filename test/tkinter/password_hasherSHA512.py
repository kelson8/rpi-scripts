'''
Reference: https://www.vitoshacademy.com/hashing-passwords-in-python/
Created by Austin Harshberger
GitHub, 2019
Free and open source
'''

# Hash password verify: https://gist.github.com/aharshbe/1ace2086b7ebe4e99a29d02e7fe83b74

# This originally wasn't created by me, I redesigned it from someone else, the original gist seems to be down.

import hashlib, binascii, os
import sys


# Create a hashed password
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


# Check hashed password validity
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


# Create password checking prompt
def password_checker(initial_password):
    password = initial_password
    storedPassowrd = hash_password(password)
    while 1:
        passowrd_input = input("Enter your computer password: ")
        checker = verify_password(storedPassowrd, passowrd_input)
        if checker:
            print("Passwords match")
            break
        else:
            print("Password incorrect, try again.")


# Run program
# initialPassword = input("Enter password to encrypt: ")
# password_checker(initialPassword)
