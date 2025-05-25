import math
def itan(x,terms):
    """
    Sums terms of Taylor series of inverse tan of x.
    """
    series_sum = 0
    for k in range(0,terms):
        series_sum = series_sum + ((-1)**k * x**(2*k+1) / (2*k+1))
    return series_sum

terms = 4
piapprox = 16 * itan(1/5,terms) - 4 * itan(1/239,terms)
print("Approximation: {}.".format(piapprox))


print("math.pi: {}.".format(math.pi))
print("Error: {}.\n".format(math.pi - piapprox))

for terms in range(1,11):
    print("{} terms:".format(terms))
    piapprox = 16 * itan(1/5,terms) - 4 * itan(1/239,terms)
    print("Approximation: {}.".format(piapprox))
    print("math.pi: {}.".format(math.pi))
    print("Error: {}.\n".format(math.pi - piapprox))
