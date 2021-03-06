def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True    

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
    
def isPalindrome(num):    
    reverse = int(str(num)[::-1])
    return num == reverse

def printDivisors(n):
    divisors = [1]
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            divisors.append(i)
            if not int(n / i) == int(i): divisors.append(int(n/i)) 
    divisors.sort()
    return divisors