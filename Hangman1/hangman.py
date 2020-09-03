#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    
    files = open(file_name, 'r')
    r = files.readlines()

    return r


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    
    length = len(words) - 1 
    a = random.randint(0, length)

    word_missing = words[a]
    length2 = len(word_missing) - 1
    b = random.randint(0, length2)

    word_missing = list(word_missing)
    word_missing[b] = '_'
    word_missing = ''.join(word_missing)
    
    print('Guess the word: ' + word_missing)

    return words[a]



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """

    answer = input("Guess the missing letter: ")

    return answer


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+ word)


if __name__ == "__main__":
    run_game('short_words.txt')

