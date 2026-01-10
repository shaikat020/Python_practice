text = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0

clean = text.lower()

for char in clean:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1 # vowel_count= vowel_count+1
        else:
            consonant_count += 1 # consonant_count= consonant_count+1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
    