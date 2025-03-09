string = input("Enter a string: ")
vowels = "aeuioAEUIO"
for char in vowels:
    string = string.replace(char, "*")
print(string)