user = input("Enter a string: ")
first_word = input("Enter the first word: ")
last_word = input("Enter the last word: ")
print(user.startswith(first_word) and user.endswith(last_word))