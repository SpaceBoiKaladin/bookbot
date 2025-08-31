#import box
from stats import get_word_count
from stats import get_character_count
from stats import book_report_num
import sys

#Funcion to get contents of book
def get_book_text(file):
    #read the .txt file. I don't actually know how this works. Should reasearch.
    with open(file) as f:
        file_contents = f.read()
    return file_contents


#Main function
def main():
    book = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
    
    #tempory code to assign pass variables around. Clean later!
    what_book = get_book_text(book)
    quantity_characters = get_character_count(what_book)
    quantity_words = get_word_count(what_book)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print(f"Found {quantity_words} total words")
    print("--------- Character Count -------")
    book_report_num(quantity_characters)
    print ("============= END ===============")


main()