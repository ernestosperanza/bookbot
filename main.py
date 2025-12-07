from stats import count_words, count_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    chars = count_char(text)
    print(f"Found {num_words} total words")
    print(chars)

main()
