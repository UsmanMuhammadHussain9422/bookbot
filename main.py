import string

def main():
    text_string = get_book_txt("books/frankenstein.txt")
    print(text_string)

def count_words(text_string):
    word_count = text_string.split()
    return len(word_count)

def get_book_txt(txt_file_Path):
    with open(txt_file_Path) as f:
        file_contents = f.read()
        return file_contents

def get_char_count(text_string):
    char_count_dic = {}
    for i in range(0, len(text_string)):
        char = text_string[i].lower()
        if char in char_count_dic :
            char_count_dic[char] += 1
        else:
            char_count_dic[char] = 1
    return char_count_dic

def get_book_report():
    text_string = get_book_txt("books/frankenstein.txt")

    word_count = count_words(text_string)
    char_count_dic = get_char_count(text_string)

    report_lines = []
    
    report_lines.append("--- Begin report of books/frankenstein.txt ---")
    report_lines.append(str.format("{0} words found in the document", word_count))    
    for char in char_count_dic:
        if string.ascii_lowercase.__contains__(char):
            report_lines.append(str.format("The '{0}' character was found {1} times", char, char_count_dic[char]))
    report_lines.append("--- End report ---")
    
    return "\n".join(report_lines)


print(get_book_report())    