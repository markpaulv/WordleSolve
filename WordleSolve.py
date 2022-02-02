import sys
import json
from typing import OrderedDict
import re
  
from collections import Counter

wordle_list = {}
clues = [('a','white'), ('s' ,'white'), ('t' , 'white'), ('e', 'yellow'), ('d', 'green')]

def read_words():
    with open('wordle_list.json') as json_file:
        word_list = json.load(json_file)
    return word_list

def normalize_clue_index(clue_index):
    if (clue_index >= 5 and clue_index < 10): 
        clue_index -= 5 
    elif (clue_index >= 10 and clue_index < 15): 
        clue_index -= 10  
    elif (clue_index >= 15 and clue_index < 20):
        clue_index -= 15  
    elif (clue_index >= 20 and clue_index < 25):
        clue_index -= 20  
    elif (clue_index >= 25 and clue_index < 30): 
        clue_index -= 25
    return clue_index

#This will check if there are more than one of the same letter in a guess, and mark the count (if not white)
def find_duplicate_clues():

    for i in range(0,25,5):
        #c = Counter(elem[0] for elem in clues[i:(i+5)])
        new_clues = {}
        for index1, tuple1 in enumerate(clues[i:(i+5)]):
            clue1 = tuple1[0]
            color1 = tuple1[1] 
            if ( (color1 != 'white') and (clue1 != '')):
                if (clue1 in new_clues.keys()):
                    new_clues[clue1] += 1
                else:
                    new_clues[clue1] = 1

        for index2, tuple2 in enumerate(clues[i:(i+5)]):
            clue2 = tuple2[0]
            color2 = tuple2[1] 
            if (clue2 in new_clues.keys() and color2 != 'white'):
                if (new_clues[clue2] > 1):
                    clues[index2+i] = (clue2+str(new_clues[clue2]   ), color2)
            elif (clue2 in new_clues.keys() and color2 == 'white'):
                clues[index2+i] = (clue2+'0', color2)                    

        new_clues.clear()
    return new_clues

def retrieve_viable_words():
    viable_words = wordle_list.copy()
    find_duplicate_clues()
    print(clues)
    for index, tuple in enumerate(clues):
        clue  = tuple[0]
        color = tuple[1]
        clue_index = normalize_clue_index(index)
        clue_count = 1
        #Checking to see if clue is a duplicate
        if (clue != '' and (re.match('\w\d', clue) != None)):
            for word in wordle_list:
                if word in viable_words.keys():
                #Get character and its index in the word string
                    clue_count = word.count(clue[0])

                    if (int(clue[1]) > clue_count):
                        viable_words.pop(word) 
                        continue
                    for i, char in enumerate(word):
                        if ((color == 'green') and (clue_index == i) and (clue[0] != char)):
                            viable_words.pop(word) 
                            break
                        elif ((color == 'yellow') and (clue_index == i) and (clue[0] == char)):
                            viable_words.pop(word)
                            break 
        #Checking to see if clue is a duplicate
        if (clue != '' and (re.match('\w\d', clue) == None)):
            for word in wordle_list:
                if word in viable_words.keys():
                #Get character and its index in the word string
                    if (color == 'yellow' and (word.count(clue) == 0)):
                        viable_words.pop(word)  
                        continue 
                    for i, char in enumerate(word):
                        #If the clue matches the char, the word cannot be valid
                        if (color == 'white' and (clue == char)):
                            viable_words.pop(word)
                            break
                        elif (color == 'yellow' and (clue_index == i) and (clue == char)):
                            viable_words.pop(word)
                            break
                        elif ((color == 'green') and (clue_index == i) and (clue != char)):
                            viable_words.pop(word)
                            break

    viable_words = OrderedDict(sorted(viable_words.items(), reverse=True, key=lambda t: t[1])) 

    return viable_words
