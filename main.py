from stats import get_num_words
from stats import get_num_characters
from stats import sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #Book text as string
    text = get_book_text(book_path)
    #call num_words function
    num_words = get_num_words(text)
    #call num_characters function
    num_chars = get_num_characters(text)
    print(num_chars)
    #call sorted_list function
    sorting_list = sorted_list(num_chars)
    print(sorting_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char,count in sorting_list:
        print(f"{char}: {count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

