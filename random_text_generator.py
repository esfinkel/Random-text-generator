# Elisabeth Finkel
# December 2017
# Credits for idea to http://www.physics.cornell.edu/~myers/teaching/ComputationalMethods/ComputerExercises/
#

import random
import string

def read_file_into_word_list(filename):
    inputFile = open(filename, 'r').read()
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    fileWL = inputFile.translate(translator)
    fileWL = fileWL.lower()
    fileWL = fileWL.replace("\xe2\x80\x99","'").replace("xe2\x80\x9d","").replace("xe2\x80\x9c","")
    fileWL = fileWL.split()
    return fileWL


def make_prefix_dictionary(filename):
    words = read_file_into_word_list(filename)
    prefix = {}
    for i in range(0, len(words)-2):
        if (words[i],words[i+1]) not in prefix:
            prefix[(words[i],words[i+1])]=[]
        prefix[(words[i],words[i+1])].append(words[i+2])
    #print prefix
    return prefix

def make_random_text(filename, num_words=100):
    """
    Input: file path + name (string). Return random_text with num_words (default 100) words.
    """
    prefix = make_prefix_dictionary(str(filename))
    current_pair = random.choice(list(prefix.keys()))
    random_text = current_pair[0] + ' ' + current_pair[1]
    for i in range(num_words-2):
        if current_pair not in prefix:
            break
            #r = random.choice(prefix.keys())
            #random_text = random_text + " " + r[1]
        else:
            r = random.choice(prefix[current_pair])
            random_text = random_text + " " + r
            rand_list = random_text.split()
            current_pair = (rand_list[i+1],rand_list[i+2])
        #print current_pair
    return random_text

if __name__ == '__main__':
    from sys import argv
    print(make_random_text(argv[0]))
