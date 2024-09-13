def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lower = lower_text(text)
    count = count_charaters(lower)
    chars_sorted_list = chars_dict_to_sorted_list(count)
    print(count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']}")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
        
def lower_text(text):
    lowered_string = text.lower()
    return lowered_string

def count_charaters(text):
    count_lower = {}
    for char in text:
        if char.isalpha():
            if char in count_lower:
                count_lower[char] += 1
            else:
                count_lower[char] = 1
    return count_lower


def sort_on(dict):
    return dict["num"]



def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch,"num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()