from stats import get_num_words
from stats import get_num_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    # print number of words in frankenstein
    #num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    #print(f"{num_words} words found in the document")
    
    # print number of characters in frankenstein
    print(get_num_chars(get_book_text("books/frankenstein.txt")))

main()