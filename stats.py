def get_word_count(text):
    num_words = 0
    for words in text.split():
        num_words +=1
    print (f"{num_words} words found in the document")

def get_character_count(text):
    letters = {}

    for character in text:
        current = character.lower()
        if current in letters:
            letters[current] +=1
        else:
            letters[current] = 1
    
    return letters

def book_report_num(unsorted_report):
    n_report = []
    for char, num in unsorted_report.items():
        if char.isalpha():
            n_report.append({"char": char, "num" : num})
    n_report.sort(reverse=True, key=lambda item: item["num"])

        
            
    return n_report