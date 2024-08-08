import math

def is_prime(n):
    """
    Basic prime testing program.
    """
    if n<2:
        return False
    i=2
    while i<=math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(2,101):
    print("{}: {}".format(i,is_prime(i)))