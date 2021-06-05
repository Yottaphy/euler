total = 0
for word in open("42_words.txt", "r").read().split(","):
    val = 0
    for letter in word:
        val += ord(letter) -64
    total += 1 if (((1 + 8*val)**0.5-1)/2) % 1 == 0 else 0    
print(total)