def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    listed_dict = dict_list(chars_dict)
    sorted = sort_dict(listed_dict)
    #print(sorted)
    print_report(sorted, book_path, num_words)

    #print(chars_dict)
    
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def dict_list(dict):
    list_of_dict = []
    for key, value in dict.items():
        if key.isalpha() == True:
            dictx = {}
            dictx["char"] = key
            dictx["num"] = value
            list_of_dict.append(dictx)
    return list_of_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(list_of_dict):
    sorted_list = sorted(list_of_dict, key=lambda x: x['num'], reverse=True)
    return sorted_list

def print_report(list, book_path, num_words):
    print("--- Begin report of "f"{book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for item in list:
        alpha = item['char']
        count = item['num']        
        print(f"The '{alpha}' character was found {count} times")
    print('--- End report ---')

main()