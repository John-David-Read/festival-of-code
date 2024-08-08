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

group1 = 0 # one more than 3k
group2 = 0 # one less than 3k

for k in range(1,101):
    if is_prime(3*k+1):
        group1 += 1
    if is_prime(3*k+2):
        group2 += 1
    if group1<=group2:
        print("At k={}: we have {} 3k+1 primes <= {} 3k+2 primes".format(k,group1,group2))
    else:
        print("Claim is false! At k={}: we have {} 3k+1 primes > {} 3k+2 primes".format(k,group1,group2))

group1 = 0 # one more than 3k
group2 = 0 # one less than 3k

for k in range(1,10**6+1):
    if is_prime(3*k+1):
        group1 += 1
    if is_prime(3*k+2):
        group2 += 1
    if group1>group2:
        print("Claim is false! At k={:,}: we have {:,} 3k+1 primes > {:,} 3k+2 primes".format(k,group1,group2))
print("At k={:,}: we have {:,} 3k+1 primes vs. {:,} 3k+2 primes".format(k,group1,group2))