"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.
    Takes a string that is a file path, opens the file, and turns the file's contents as one string of text."""
    with open(file_path) as f:
        read_data = f.read()
        return read_data

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys()) 
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    
    #creating a dictionary
    # #cut the string into a list of strings
    # words = text.split()
    # #iterate through the list 
    #     #for idx, num in range(len(words)):
    # for i in range(len(words) - 2)
    # #potential key is first word, second word, in a tuple 
    # tup_key = (words[i], words[i + 1])
    #value is a the third word, which we want to put into a list 
    # value is a list
    #if the key is already in the dictionary
        #add the value to the list stored at that key in the dictionary 
    #if the key is not in the dictionary yet
        #add the key to the dictionary, have an empty list as the value 
        #add the string value to that list 
    #return the dictionary 
    chains = {}

    text = open_and_read_file("green-eggs.txt")
    text_string = text.split()
    
    for i in range(len(text_string)-2):
        tup_key = (text_string[i], text_string[i+1])
        str_val = [text_string[i+2]]
        #if tup_key not in chains:
        chains[tup_key] = str_val
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = choice(list(chains.keys()))
    #print(random_key)

    random_value = chains[random_key]
    #print(first_string)

    first_string_of_words = list(random_key)
    first_string_of_words = (first_string_of_words + random_value)
    print(first_string_of_words)
    
    for i, word in enumerate(first_string_of_words):
        key = (words[i + 1], words[i + 2])
        value = chains[key]
        first_string_of_words.append(value)
    
    # second_key = (first_string_of_words[1], first_string_of_words[2])
    # second_string = chains[second_key]
    # print(second_string)

    



    # container.append(random_key[0])
    # container.append(random_key[1])
    #print(container)
    #print(container[0] + " "
    #      + container[1])
    
    #for words in list(chains)
    
    #starting_point = chains[0]
    # print(chains{[0]}
    # print(starting_point)
    
    #for i, collection in enumerate(chains): 
    # #    print("The {collection}'s index is {i}")

    # keys_only = chains.keys()
    # keys_only = keys_only.items()
    # print(keys_only[0])
    
    # list(chains[tup_key[0]])
    
    
    #return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)