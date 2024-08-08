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

current = str(6567629137)

while current != "":
    if is_prime(int(current)):
        print("{} is prime".format(current))
    else:
        print("{} is not prime".format(current))
        break
    current = current[1:]