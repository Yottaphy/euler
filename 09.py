def isTriplet(a,b,c):
    return (a**2 + b**2) == c**2


for a in range(1,1001):
    for b in range(a+1,1001):
        c = 1000 - (a+b)
        if isTriplet(a,b,c): print(a,b,c,a*b*c)