from eulerfuncs import isPrime

n             = 1
pct           = 1
total_corners = 1
number_primes = 0

while pct >= 0.1:
    l = 2*n + 1
    total_corners += 4
    if isPrime(l**2 - 1*l + 1): number_primes+=1
    if isPrime(l**2 - 2*l + 2): number_primes+=1
    if isPrime(l**2 - 3*l + 3): number_primes+=1
    pct = number_primes / total_corners
    n+=1

print(l)