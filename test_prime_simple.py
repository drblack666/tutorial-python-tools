from Prime import isPrime
import time

def test_small_0():
    assert isPrime(0) == False

def test_small_1():
    assert isPrime(1) == True

def test_small_negative():
    assert isPrime(-7) == True
