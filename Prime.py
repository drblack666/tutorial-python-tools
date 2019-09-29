def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
    
    
def test_small_2():
    assert isPrime(2) == False

def test_small_3():
    assert isPrime(3) == True

def test_small_21():
    assert isPrime(21) == False
