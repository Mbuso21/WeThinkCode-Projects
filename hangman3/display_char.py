import random

global random_letter

def random_fill_word(word):

    random_letter = random.randint(0, len(word) - 1)
    word = list(word)
    #ran_index = word.index(word[random_letter])
    strlen  = 0
    count = len(word)

    while count > 0:
        if strlen != random_letter:
            word[strlen] = '_'
        count -= 1
        strlen += 1

    word = "".join(word)

    return word

    #print(word[random_letter])
    #print(word)

#random_fill_word('feet')


#print(random_fill_word('feet'))