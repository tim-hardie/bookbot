def get_num_words(book_contents):
    words_list = book_contents.split()
    
    return len(words_list)

def get_num_chars(book_text):
    char_dict = {}
    
    for c in book_text:
        if c.lower() in char_dict:
            char_dict[c.lower()] += 1
        else:
            char_dict[c.lower()] = 1
    
    return char_dict