PATH = "words.txt"
WHITESPACE = " "

def get_word():
    """
    Displays message to the user and waits
    for the user input
    """
    anagram = input("Please input anagram: ")
    
    return anagram 

def check_anagram(word):
    """
    Checks if the user has input valid anagram.

    Valid anagram can contain only letters and spaces.

    It shouldn't matter if some letter is capital or not.
    """

    check = True
    for letter in word:
        if not (letter.isalpha() or letter.isspace()):
            check = False

    return check

def load_words():
    """
    Opens the file specified by PATH and loads all the 
    words from file into the words list nad returns it.
    """

    words = []
    with open(PATH) as word_file:
        for line in word_file:
            #? we use strip to remove unnecessary whitespaces
            words.append(line.strip())

    return words

def sort_word(word):
    """
    Sorts the letters in word alphabetically and returns
    the newly sorted word.

    It should remove whitespaces and convert all characters to lowercase.
    """

    #? python allows us to cast string into list of chars
    #? you can sort lists by default in python by calling .sort() method
    #? We use .lower() here because you can have for example 'A' and 'a' and those are not the same letters
    word_list = list(word.lower())
    word_list.sort()
    
    sorted_word = ""
    for letter in word_list:
        if letter != WHITESPACE:
            sorted_word += letter
    
    return sorted_word

def find_matching_words(anagram, word_list):
    """
    Finds the words which can be created by rearranging anagram.
    
    Returns list of viable words.
    
    If there are no such words, it returns an empty list.
    """
    viable_words = []
    for word in word_list:
        if sort_word(anagram) == sort_word(word):
            viable_words.append(word)
    
    return viable_words

def main():
    #? Initialzation part here
    #? You have to take anagram from user and check if it's a valid anagram. Repeat the input as long as the anagram is invalid.
    #? You have to load the words form the words.txt file
    #? You have to sort letters in each word by alphabetical order
    #? You also have to sort anagram which user has input and remove any spaces
    #? If your sorted anagram is equal to one or more sorted words from the words list, then you should display those words
    #? If there are no words which meet the criteria you should display a proper message to the user
    
if __name__ == "__main__":
    main()