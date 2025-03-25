def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():  # Convert text to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_char_count(char_count_dict):
    sorted_list = []
    for char in char_count_dict:
        sorted_list.append({"char": char,"num": char_count_dict[char]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list