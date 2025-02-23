from collections import Counter

def check_or_create_file():
    try:
        with open("sample.txt", "r"):
            pass
    except FileNotFoundError:
         print("The file 'sample.txt' does not exist. Please type a paragraph to create the file.")
         user_input = input("Enter a paragraph: ")
         with open("sample.txt", "w") as f:
             f.write(user_input)

def read_and_process_file():
    with open("sample.txt","r") as f:
        text = f.read()
    punctuations = ['.', ',', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '"', "'", '-']
    for p in punctuations:
        text = text.replace(p,'')
        clean_text = text.lower()
        words = clean_text.split()
        return words
def count_word_frequencies(words):
    word_count = Counter(words)
    return word_count
def display_results(word_count):
    total_words = sum(word_count.values())
    print(f"Total Words: {total_words}")
    most_common_words = word_count.most_common(5)

    with open("sample.txt","w") as f:
        f.write("Word Count report\n")
        f.write(f"Total words: {total_words}\n")
        for word, count in most_common_words:
            f.write(f"{word}-{count}\n")
    
def main():
    check_or_create_file()
    words = read_and_process_file()
    word_count = count_word_frequencies(words)
    display_results(word_count)

if __name__=="__main__":
    main()