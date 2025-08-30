#import box
from stats import get_word_count
from stats import get_character_count
from stats import book_report_num

#Funcion to get contents of book
def get_book_text(file):
    #read the .txt file. I don't actually know how this works. Should reasearch.
    with open(file) as f:
        file_contents = f.read()
    return file_contents


#Main function
def main(book):
    #tempory code to assign pass variables around. Clean later!
    temp = get_book_text(book)
    temp2 = get_character_count(temp)
    print(book_report_num(temp2))


main("./books/frankenstein.txt")