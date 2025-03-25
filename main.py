from stats import get_word_count, get_sorted_char_count, get_char_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    
    book_text = get_book_text(path_to_file)
    word_count = get_word_count(book_text)
    char_count_dict = get_char_count(book_text)
    sorted_char_count = get_sorted_char_count(char_count_dict)
    print_report(path_to_file, word_count, sorted_char_count)


def print_report(book_path, word_count, sorted_char_count):
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}")
    print("---------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("---------- Character Count----------")
    for char in sorted_char_count:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")

main()

