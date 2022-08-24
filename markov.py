"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    the_file = open(file_path).read()


    return the_file
#print(open_and_read_file("/Users/drjafer/src/markov-chains/green-eggs.txt"))
    


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    input: This is a test as well This is computer
    output: chain = {(This, is): [a, computer, apple, coding]
                     (is, a): [test]
                     (a, test): [as]
                     (test, as): [well]
                     (as, well): [This]}

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

    #step1 : how to iterate over the given text and separate the words
    #step2 : iterate and save index 0 as the first item of tuple, and index 1 as the second item of item.
    #step3: Check if the tuple already exists in the chains dictionary as key, if not exists, than add it. 



    chains = {}

    words = text_string.split()
   

     #input: [This, is, a, test, as, well, This, is, computer]
    #  range(len(input))

    for i in range(len(words) - 2):
        index = (words[i] , words[i +1])
        if index not in chains:
            chains[index] = [words[i + 2]]
        else:
            chains[index].append([words[i + 2]])


    return chains

#print(make_chains(open_and_read_file("/Users/drjafer/src/markov-chains/green-eggs.txt")))



# a = [c,d]
# a.append(f)
# a = [c,d,f]

# x[b] = [1,3]

# x = {b: [1,3]}
# x[b].append(4)

# x = {b: [1,3,4]}


# chain = {(8,9): [4,56,7,10]
#          (1,2): "this is a test"}

# key = (1,2), (3,4), (5,6)
# if key not in chain:
#     chain[key] = "This is a test"
# else: 
#     chain[key].append(word[1+2])








def make_text(chains):
    """Return text from chains.
    
    input: chain = {(this, is): [a, was, prepared]
                    (is, computer): [would, could]}

    output: [is, computer, could]
    """

    chains = open_and_read_file("/Users/drjafer/src/markov-chains/green-eggs.txt")
    chained_dictionary = make_chains(chains)

    
    words = []
    all_keys = []

    for key, value in chained_dictionary.items():
        all_keys.append(key)
    
    random_key = choice(all_keys)
    words.append(random_key)


    for key, value in chained_dictionary.items():
        if random_key == key:
            random_value = choice(value)
            words.append(random_value)

    
    additional_dic = (words[0], words[1])

    for key, value in chained_dictionary.items():
        if key not in chained_dictionary:
            chained_dictionary[additional_dic] = choice(value)
        else:
            pass

        # print(f"{key[0]} {key[1]} {value[0]}")

    

    # your code goes here

    # return ' '.join(words)


# print(make_text("/Users/drjafer/src/markov-chains/green-eggs.txt"))


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
