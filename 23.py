from math import sqrt
import time

# LONG PROGRAM - POSSIBLY BRUTE FORCE


def printDivisors(n):
    divisors = [1]
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            divisors.append(i)
            if not int(n / i) == int(i): divisors.append(int(n/i)) 
    divisors.sort()
    return divisors

def isAbundant(n):
    Sum = sum(printDivisors(n))
    check = Sum / n 
    if check > 1: return True
    else: return False

listAbundant = []

for i in range(1, 28112):
    if isAbundant(i): listAbundant.append(i)

total = 0
for i in range(1, 28124):
    for j in range(1, int(i/2)+1): 
        if j not in listAbundant: continue
        else: 
            if int(i - j) in listAbundant: break
    else:
        total += i

print(total)

 