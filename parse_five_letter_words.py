import json
#This file parses all five letter words from the word list

freq_map = {'e' : 57, 'a' : 43, 'r' : 39, 'i' :  38, 'o' : 37, 't' : 35,'n' : 34, 's' : 29, 'l' : 28, 'c' : 23, 'u' : 19, 'd' : 17, 'p' : 16, 
            'm' : 15, 'h' : 15, 'g' : 12, 'b' : 10, 'f' : 9, 'y' : 9, 'w' : 6, 'k' : 5, 'v' : 5, 'x' : 1, 'z' : 1, 'j' : 1, 'q' : 1}

def load_words():
    with open('enable1.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def parse_five_letter_words(words):
    five_letter_word_list = []
    for word in words:
        if len(word) == 5:
            five_letter_word_list.append(word)

    return five_letter_word_list

def add_letter_frequency(words):
    dict_of_words = {}
    for word in words:
        dict_of_words[word] = 0
        for char in word:
            dict_of_words[word] += freq_map.get(char)
            dict_of_words[word] -= word.count(char)*12
        if dict_of_words[word] < 0:
            dict_of_words[word] = 0

    return dict_of_words

if __name__ == '__main__':
    english_words = load_words()
    five_letter_english_words = parse_five_letter_words(english_words)
    five_letter_words_with_freq = add_letter_frequency(five_letter_english_words)
    #Write to new file
    textfile = open("wordle_list.json", "w")
    textfile.write(json.dumps(five_letter_words_with_freq))
    textfile.close()
