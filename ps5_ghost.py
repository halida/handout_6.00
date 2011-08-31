# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 0:38
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def run_game(get_input):
    word_fragment = ''
    current_player = 2
    first = True
    
    print "Welcome to Ghost!"
    print "Player 1 goes first."
    print "Current word fragment: '%s'" % word_fragment.upper()

    while True:
        current_player = current_player %2 + 1
        if not first:
            print "Player %d's turn." % current_player
        first = False
        
        letter = get_input("Player %d says letter: " % current_player)
        letter = letter.lower()

        # check letter
        if len(letter) != 1 or letter not in string.ascii_letters:
            print "wrong letter: %s" % letter
            continue
        word_fragment = word_fragment + letter
        print "Current word fragment: '%s'" % word_fragment.upper()

        # check word
        for word in wordlist:
            if word == word_fragment:
                print "Player %d loses because '%s' is a word!" % (current_player, word.upper())
                print "Player %d wins!" % (current_player % 2 + 1)
                return
            if word.startswith(word_fragment):
                break
        else:
            print "Player %d loses because no word begins with '%s'!" % (current_player, word_fragment.upper())
            print "Player %d wins!" % (current_player % 2 + 1)
            return

def get_fake_input(v):
    l = [0, ]
    def f(desc, l=l):
        o =  v[l[0]]
        print desc + o
        l[0] += 1
        return o
    return f

vs1 = 'PYTHON'
vs2 = 'PYN'

def test():
    """
    >>> run_game(get_fake_input(vs1))
    Welcome to Ghost!
    Player 1 goes first.
    Current word fragment: ''
    Player 1 says letter: P
    Current word fragment: 'P'
    Player 2's turn.
    Player 2 says letter: Y
    Current word fragment: 'PY'
    Player 1's turn.
    Player 1 says letter: T
    Current word fragment: 'PYT'
    Player 2's turn.
    Player 2 says letter: H
    Current word fragment: 'PYTH'
    Player 1's turn.
    Player 1 says letter: O
    Current word fragment: 'PYTHO'
    Player 2's turn.
    Player 2 says letter: N
    Current word fragment: 'PYTHON'
    Player 2 loses because 'PYTHON' is a word!
    Player 1 wins!
    >>> run_game(get_fake_input(vs2))
    Welcome to Ghost!
    Player 1 goes first.
    Current word fragment: ''
    Player 1 says letter: P
    Current word fragment: 'P'
    Player 2's turn.
    Player 2 says letter: Y
    Current word fragment: 'PY'
    Player 1's turn.
    Player 1 says letter: N
    Current word fragment: 'PYN'
    Player 1 loses because no word begins with 'PYN'!
    Player 2 wins!
    """
    import doctest
    doctest.testmod()

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        test()
    else:
        run_game(raw_input)
    
if __name__=="__main__":
    main()
