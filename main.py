from stats import get_word_count

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents


def main(book):
    temp = get_book_text(book)
    get_word_count(temp)


main("./books/frankenstein.txt")