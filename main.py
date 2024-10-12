import os

def file_check(path):
    if os.path.isfile(path):
        return True
    else:
        print("The file does not exist!")
        return False

def main():
    book_path = "books/frankenstein.txt"
    if file_check(book_path):
        text = get_book_text(book_path)
        word_count = number_of_words(text)
        character_dictionary = count_characters(text)
        print(f"The book contains {word_count} words.")
        print("\nCharacter counts:")
        for char, count in character_dictionary:
            print(f"The character '{char}' appears {count} times")

def get_book_text(path):
    print(f"Reading from: {path}")
    with open(path, "r") as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

def count_characters(text):
    lower_case_text = text.lower()
    character_tracker = {}
    character_list = []
    for char in lower_case_text:
        if char.isalpha():
            character_tracker[char] = character_tracker.get(char, 0) + 1

    for char, count in character_tracker.items():
        character_list.append((char, count))
    
    character_list.sort(key=lambda x: x[1], reverse=True)


    return character_list

main()