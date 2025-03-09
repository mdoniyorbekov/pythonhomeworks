vowels = "aeiouAEIOU"
user = input("Enter a string: ")
vowel_numbers = sum(1 for char in user if char in vowels)
consonant_numbers = sum(1 for char in user if char not in vowels)
print (f"""vowels: {vowel_numbers} 
consonants: {consonant_numbers}""")