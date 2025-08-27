def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(text):
    num_words = 0
    for words in text.split():
        num_words +=1
    print (f"{num_words} words found in the document")

def main(book):
    temp = get_book_text(book)
    get_word_count(temp)


main("./books/frankenstein.txt")