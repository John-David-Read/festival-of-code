"""
Generates elements 0<a,b,c,d,e,f,g,h<10 for matrices such that 
a b  *  e f  =  10a+e   10b+f
c d     g h     10c+g   10d+h
"""

r = open(r"Resource\results.txt","w")

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                n = a*d-a-b*c-d + 1
                if n != 0:
                    e = 10*(a*d-a-b*c) / n
                    f = - 10*b / n
                    g = - 10*c / n
                    h = - 10*(b*c+d-a*d) / n
                    if e == int(e) and f == int(f) and g == int(g) and h == int(h): # check integer solutions
                        if 0<e<10 and 0<f<10 and 0<g<10 and 0<h<10: # limit to 1-9 like a,b,c,d are
                            if a!=e or b!=f or c!=g or d!=h: # remove the ones where it's a matrix squared because it looks like some weird symmetry trick
                                if a!=c or b!=d or e!=g or f!=h: # remove ones where it's the same rows repeated
                                    r.write(f"{a},{b},{c},{d},{int(e)},{int(f)},{int(g)},{int(h)}\n")

r.close()