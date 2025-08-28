from stats import get_word_count
from stats import get_character_count
from stats import book_report_num

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main(book):
    temp = get_book_text(book)
    temp2 = get_character_count(temp)
    print(book_report_num(temp2))


main("./books/frankenstein.txt")