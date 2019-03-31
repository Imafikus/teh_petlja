PATH = "words.txt"

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


def main():
    #? Initialzation part here
    #? You have to take anagram from user and check if it's a valid anagram
    #? You have to load the words form 

if __name__ == "__main__":
    main()