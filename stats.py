def count_words(book_text):
    words = book_text.split()  # Split the text into words based on whitespace 
    return len(words)  # Return the number of words

def count_characters(book_text):
    char_count = {}
    for char in book_text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def char_list_sorted(char_count):
    sorted_chars = []
    for char, counter in char_count.items():
	    sorted_chars.append({"character": char, "count": counter})
    
    sorted_chars.sort(key=lambda item: item["count"], reverse=True)

    return sorted_chars
   


