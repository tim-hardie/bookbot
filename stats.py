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

def sort_char_dict(char_dict):
    sorted_char_list = []
    for char in char_dict:
        num = char_dict[char]
        sorted_char_list.append({"char": char, "num": num})

    def sort_on(items):
        return items["num"]
    sorted_char_list.sort(reverse=True, key=sort_on)
    
    return sorted_char_list