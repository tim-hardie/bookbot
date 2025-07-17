from stats import get_num_words
from stats import get_num_chars
from stats import sort_char_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    
    # print number of words in frankenstein
    print("----------- Word Count ----------")
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")
    
    # print number of characters in frankenstein
    #num_chars = get_num_chars(file_contents)
    #print(num_chars)

    # sort dict of characters
    print("--------- Character Count -------")
    char_list_sorted = sort_char_dict(get_num_chars(file_contents))
    for i in range(0,len(char_list_sorted)):
        if char_list_sorted[i]["char"].isalpha():
            print(f"{char_list_sorted[i]["char"]}: {char_list_sorted[i]["num"]}")
    
    print("============= END ===============")

main()
