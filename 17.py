def spell(n):
    digits= {0: '', 1: 'one', 2: 'two', 3: 'three', 4:'four', 5:'five', 6:'six',7:'seven',8:'eight',9:'nine',10: 'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen',18:'eighteen', 19:'nineteen',20: 'twenty', 30: 'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',80:'eighty', 90:'ninety'}

    if n <= 20:
        return digits[n]
    if n == 1000: return 'onethousand'
    if n < 100: return digits[10*int(n/10)]+digits[n%10]
    if n%100 == 0: return digits[int(n/100)]+'hundred'
    return digits[int(n/100)]+'hundredand'+spell(n-100*int(n/100))

chain = ''
for i in range(1,1001):
    chain += spell(i)
    print(spell(i))
print(len(chain))