# Elisabeth Finkel
# December 2017; modified November 2018
# Credits for idea to http://www.physics.cornell.edu/~myers/teaching/ComputationalMethods/ComputerExercises/
#

import random
import string

def read_file_into_word_list(filename):
    inputFile = open(filename, 'r').read()
    fileWL = inputFile.encode().decode('ascii',errors='ignore')
    fileWL = fileWL.replace(',','').replace('.','').replace('"','').replace(':','').replace('-','').replace('!','').replace('(','').replace(')','')
    fileWL = fileWL.lower().split()
    return fileWL


def make_big_prefix_dictionary(filename):
    words = read_file_into_word_list(filename)
    prefix = {}
    for i in range(0, len(words)-3):
        if (words[i],words[i+1],words[i+2]) not in prefix:
            prefix[(words[i],words[i+1],words[i+2])]=[]
        prefix[(words[i],words[i+1],words[i+2])].append(words[i+3])
    #print prefix
    return prefix

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
    #prefix = make_prefix_dictionary(str(filename))
    big_prefix = make_big_prefix_dictionary(str(filename))
    current_set = random.choice(list(big_prefix.keys()))
    random_text = current_set[0] + ' ' + current_set[1] + ' ' + current_set[2]
    for i in range(num_words-3):
        if current_set in big_prefix:
            r = random.choice(big_prefix[current_set])
            random_text += ' ' + r
            current_set = (current_set[-2],current_set[-1],r)
            #current_set = (rand_list[-3],rand_list[-2],rand_list[-1])
    return random_text



if __name__ == '__main__':
    from sys import argv
    x = 100
    if argv[2].isdigit():
        x = int(argv[2])
    print(make_random_text(argv[1],x))