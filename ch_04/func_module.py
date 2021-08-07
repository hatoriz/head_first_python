def search4vowels(word) -> object:
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)

word = "I am Nathdanai Toon"
search4vowels(word)