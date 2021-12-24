#figured that the discriminant (b^2 -4ac) always gave -163. Tried all combinations with a pos and neg. the one with the highest |a| had to be the answer.

thelist = []
for b in range(1000,0,-1):
    a = (4*b -163)**0.5
    if b < 163/3: break
    if a %1 == 0:
        print(a, b, a*b)
        print(-a, b, -a*b)
        break