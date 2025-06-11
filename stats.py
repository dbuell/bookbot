def get_book_number_of_words(book_text):
    words = book_text.split()
    return len(words)


def char_count(book_text):
    words = book_text.split()
    c_count = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char.isalpha():
                if char in c_count:
                    c_count[char] += 1
                else:
                    c_count[char] = 1
    return c_count

def sort_on(dict):
    return dict["num"]

def char_sorted(char_count_dict):
    char_dict = []
    for char in char_count_dict:
        char_dict.append({"char": char, "num": char_count_dict[char]})
    char_dict.sort(reverse=True, key=sort_on)
    return char_dict