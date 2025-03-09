sentence = input("Enter a sentence: ")
print("".join(word[0].upper() for word in sentence.split()))