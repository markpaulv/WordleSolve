#This file parses all five letter words from the word list
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def parse_five_letter_words(words):
    five_letter_word_list = []
    for word in words:
        if len(word) == 5:
            five_letter_word_list.append(word)

    return five_letter_word_list

if __name__ == '__main__':
    english_words = load_words()
    five_letter_english_words = parse_five_letter_words(english_words)
    #Write to new file
    textfile = open("wordle_list.txt", "w")
    for word in five_letter_english_words:
        textfile.write(word + "\n")

    textfile.close()
