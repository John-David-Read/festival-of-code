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

for n in range(2,1001):
    current = str(n)

    is_right_trunc_prime = True

    while current != "":
        if not is_prime(int(current)):
            is_right_trunc_prime = False
            break
        current = current[:-1]

    if is_right_trunc_prime:
        print(n)