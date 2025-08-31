def get_word_count(text):
    #initalize empty word count
    num_words = 0

    #iterate text
    for words in text.split():
        #update quantity
        num_words +=1
    
    #output quantity
    #print (f"{num_words} words found in the document")
    return num_words

def get_character_count(text):
    #create empty dictionary
    letters = {}

    #iterate through text
    for character in text:
        #lowercase letters only
        current = character.lower()

        #update quantity, add if it's not there
        if current in letters:
            letters[current] +=1
        else:
            letters[current] = 1
    
    #return the dictionary
    return letters

def book_report_num(unsorted_report):
    n_report = []
    for char, num in unsorted_report.items():
        if char.isalpha():
            n_report.append({"char": char, "num" : num})
    n_report.sort(reverse=True, key=lambda item: item["num"])

    for item in n_report:
        print(f"{item['char']}: {item['num']}")



# tip from Boots
#   in main.py, print the headers.
#   Print total word count.
#   Loop your sorted list and print lines like:
#
#       for item in sorted_chars:
#           print(f"{item['char']}: {item['num']}")