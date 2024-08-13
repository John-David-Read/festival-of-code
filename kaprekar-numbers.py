def int_to_list(n):
    return list(map(int,str(n)))

def list_to_int(ns):
    return int(''.join(map(str, ns)))

def is_kaprekar(n):
    if n**2 < 10:
        if n**2 == n:
            print("({})".format(n),"+", "({})".format(0),"=",n)
        return 
    nn = len(int_to_list(n))    # Digits of the number
    d = int_to_list(n**2)       # Square
    d_l = d[:-nn]               # Left side
    d_r = d[-nn:]               # Right side

    # Right term can't be zero (by convention)
    if d_r == 0:
        return False

    if (n==list_to_int(d_l) + list_to_int(d_r)):
        print("({})".format(list_to_int(d_l)),"+", "({})".format(list_to_int(d_r)),"=",list_to_int(d_l) + list_to_int(d_r))

    return

n = 1
while n<1000000:
    is_kaprekar(n)
    n = n+1
