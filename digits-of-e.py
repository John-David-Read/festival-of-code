from math import exp

def factorial(n):
    """
    Recursive program to calculate n! for input n.
    """
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)

def expo(x,terms):
    """
    Sums terms of Taylor series of e**x.
    """
    series_sum = 0
    for k in range(0,terms):
        series_sum += x**k / factorial(k)
    return series_sum

for terms in range(1,19):
    print("{} terms:".format(terms))
    expapprox = expo(1,terms)
    print("Approximation: {}.".format(expapprox))
    print("math.pi: {}.".format(exp(1)))
    print("Error: {}.\n".format(exp(1) - expapprox))