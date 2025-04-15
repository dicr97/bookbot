import sys
def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

from stats import count_words, count_characters, char_list_sorted

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    
    # Count the words
    word_count = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = count_characters(book_text)
    sorted_chars = char_list_sorted(char_counts)
    for item in  sorted_chars:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")


# Calling the main function to execute the program
if __name__ == "__main__":
    main()

