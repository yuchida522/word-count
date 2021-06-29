import re
def word_count(text, freq_word, integer): 

    freq_word_set = set()
    with open(freq_word) as freq_word_file:
        for line in freq_word_file:
            freq_word_set.add(line.rstrip().lower())

    word_count = {}

    with open(text) as file:
        for line in file:
            line_stripped = line.lower().replace(',', '').replace('.', '').strip()
            words = re.sub(r'[^\w\d\s\']+', '', line_stripped).split()
            # print(words)
            for word in words:
                if word not in freq_word_set:
                    word_count[word] = word_count.get(word, 0) + 1
    
    
    sorted_dict = sorted(word_count.items(), key=lambda item:item[1], reverse=True)

    top_words = sorted_dict[:integer]

    for word in top_words:
        print(word[1], word[0])
    
word_count('alice_in_wonderland.txt', '1-1000.txt', 10)
