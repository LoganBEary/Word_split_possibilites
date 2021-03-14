import sys


def split(word, dictionary, variations, spacedWord=''):
    """
    Splits the line up into various possible options
    :param variations: array of possible variations
    :param word: current line being split with spaces
    :param dictionary: list of possible words
    :param spacedWord: separator to add in between all words that are within the dictionary
    :return: multiple lines with properly spaced words
    """
    # when reaching the end of the string - Print possible string splits
    if not word:
        variations.append(spacedWord)
    # go throughout entire string
    for idx in range(1, len(word) + 1):
        # get the string from current start to end of string
        current = word[:idx]
        # check each time if current string is a word
        # in that section of dictionary
        letterSection = dictionary[current[0]]
        # if it is, then call split again adding a space
        if current in letterSection:
            split(word[idx:], dictionary, variations, spacedWord + " " + current)


# helper function to add word to correct key
def addToDictionary(currentLine, dictionary):
    """
    Helper function to add words to map depending on first letter
    :param currentLine: current word being added
    :param dictionary: list of words sorted by first letter
    :return: updated dictionary containing words corresponding to first letter
    """
    for currentKey in dictionary.keys():
        # if first letter corresponds to the key, insert it
        if currentLine[0] == currentKey:
            dictionary[currentKey].append(currentLine.strip('\n'))


def dictionaryContains(theWord, dictionary):
    letter = theWord[0]
    for idx in dictionary[letter]:
        if idx == theWord:
            return True
    return False


def wordBreak(theCurrentLine, dictionary):
    """
    determines if line is able to be split up properly into separate words
    :param theCurrentLine: current word to see if splittable
    :param dictionary: dictionary containing all words to compare too
    :return: boolean - True/False
    """
    # bottom up approach
    if len(theCurrentLine) == 0:
        return True
    # set array to all False
    dp = [False for idx in range(0, (len(theCurrentLine) + 1))]
    # set initial value to True
    dp[0] = True
    # go through entire line
    for curr in range(1, len(theCurrentLine) + 1):
        # start at beginning of each segment
        for y in range(curr - 1, -1, -1):
            # if it contains a word and the previous one was true - Set it as true
            if dp[y] and dictionaryContains(theCurrentLine[y:curr], dictionary):
                dp[curr] = True
    # return last index dictating if its splittable
    return dp[len(theCurrentLine)]


if __name__ == 'main':
    """
    Read info from file 
    set dictionary specifically to diction21.txt - per Handout
    read file and determine if words can be split up
    """
# create dictionary of words in dictionary file
a_dictionary = open("diction10k.txt", "r")
# create each key as each letter in alphabet - speed up search time complexity
dictionary_map = {chr(ord('a') + i): [] for i in range(26)}

# add correct words corresponding to first letter in word
for line in a_dictionary:
    addToDictionary(line, dictionary_map)
# read lines from file
file = sys.stdin.readlines()
# strip \n from lines
file = [line.strip('\n') for line in file]
# get C for length of file
theLine = int(file[0]) + 1
# for each line check if it can be split
for x in range(1, theLine):
    variation = []
    if wordBreak(file[x], dictionary_map):
        print("\nphrase", x)
        print(file[x], "\n")
        print("output", x)
        print("Yes, you can split")
        split(file[x], dictionary_map, variation, spacedWord='')
        print(variation.pop())
    else:
        print("\nphrase", x)
        print(file[x])
        print("No, you cannot split\n")
