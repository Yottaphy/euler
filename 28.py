total = 1
l     = 1
n     = 1

while l < 1001:
    l = 2*n + 1    
    total+= 4*l**2 - 6*l + 6
    n+=1

print(l, total)