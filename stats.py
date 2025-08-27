def get_word_count(text):
    num_words = 0
    for words in text.split():
        num_words +=1
    print (f"{num_words} words found in the document")