from stats import count_words, count_char, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def generate_report(book_path):
    text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    chars = count_char(text)
    list = chars_dict_to_sorted_list(chars)
    for char in list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
        else:
            continue 

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        generate_report(path)

main()
