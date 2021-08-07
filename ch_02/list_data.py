vowels = ['a', 'e', 'i', 'o', 'u']

word = "Haaatoriz"
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print("Print only vowel")
for vowel in found:
    print(vowel)