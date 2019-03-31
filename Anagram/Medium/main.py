PATH = "words.txt"
WHITESPACE = " "

def get_word():
    """
    Displays message to the user and waits
    for the user input
    """
    pass    

def check_anagram(word):
    """
    Checks if the user has input valid anagram.

    Valid anagram can contain only letters and spaces.

    It shouldn't matter if some letter is capital or not.
    """
    pass

def load_words():
    """
    Opens the file specified by PATH and loads all the 
    words from file into the words list nad returns it.
    """
    pass

def sort_word(word):
    """
    Sorts the letters in word alphabetically and returns
    the newly sorted word.

    It should remove whitespaces and convert all characters to lowercase.
    """
    pass

def find_matching_words(anagram, word_list):
    """
    Finds the words which can be created by rearranging anagram.
    
    Returns list of viable words.
    
    If there are no such words, it returns an empty list.
    """
    pass

def main():
    #? Initialzation part here
    #? You have to take anagram from user and check if it's a valid anagram. Repeat the input as long as the anagram is invalid.
    #? You have to load the words form the words.txt file
    #? You have to sort letters in each word by alphabetical order
    #? You also have to sort anagram which user has input and remove any spaces
    #? If your sorted anagram is equal to one or more sorted words from the words list, then you should display those words
    #? If there are no words which meet the criteria you should display a proper message to the user
    pass
    
if __name__ == "__main__":
    main()