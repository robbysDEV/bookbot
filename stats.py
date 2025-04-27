def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    chars = {}
    lower_text = text.lower()
    for i in lower_text:
        if i.isalpha():
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
    return chars

def sorted_list(chars):
    list_sort= []
    for i in chars:
        list_sort.append((i,chars[i]))
        list_sort.sort(key=lambda pair: pair[1], reverse=True)
    return list_sort



