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
