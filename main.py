from stats import get_book_number_of_words
from stats import char_count
from stats import char_sorted

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content
    



def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    words = get_book_number_of_words(book_text)
    #print(f"{words} words found in the document.")
    char_count_dict = char_count(book_text)
    #print(char_count_dict)
    sorted_char_count = char_sorted(char_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()