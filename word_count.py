'''
running instructions

1. requirements
    > python3
    > the two files, text file and common words file, must be placed in the same directory as this file
2. How to run
    > clone this repo
    > Please make sure that the two text files (file to look through, list of common words) are in the same directory as this file
    > In your terminal, run '$ python3 word_count.py'
    > Enter the information as prompted


'''
import re
def word_count(text, freq_word, n): 

    #setting the common words list into a set so it can be looked up
    freq_word_set = set()
    with open(freq_word) as freq_word_file:
        for line in freq_word_file:
            freq_word_set.add(line.rstrip().lower())

    #where the word count will be stored
    word_count = {}

    with open(text) as file:
        for line in file:
            #I am making all the words lower case, where I am making the assumption that capitalization is not necessary (ex. alice == Alice)
            line_stripped = line.lower().strip()
            #getting rid of all punctuation, except for apostrophies (ex. won't it's)
            words = re.sub(r'[^\w\d\s\']+', '', line_stripped).split()
            for word in words:
                if word not in freq_word_set:
                    word_count[word] = word_count.get(word, 0) + 1
    
    #sort the dictionary 
    sorted_dict = sorted(word_count.items(), key=lambda item:item[1], reverse=True)

    #take only the top n words given from the user input
    top_words = sorted_dict[:n]
    print("Count", "Word")
    print("===", " ===")
    for word in top_words:
        print(word[1], " ", word[0])

def run_program():
    ''' takes user inputs '''
    while True:
        content_file = input("Name of file to parse through: ")
        if not content_file:
            continue
        else:
            break
    while True:
        common_words_file = input("Name of the common words file: ")
        if not common_words_file:
            continue
        else:
            break
    while True:
        num = input("How many top common words would you like to see?: ")
        if not num:
            continue
        else: 
            break
    try:
        word_count(content_file, common_words_file, int(num))
    except:
        print("You are missing information, please try again")

run_program()

