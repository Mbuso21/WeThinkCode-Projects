import random
from display_char import random_fill_word

original_word = 'feet'
answer_word = random_fill_word(original_word)

char_list = 'abcdefghijklmnop'
input_char =  input('Enter letter: ')

print(answer_word)

def is_missing_char(original_word, answer_word, char):
    i = 0
    for chara in original_word:
        if chara == char and  answer_word[i] == '_':
            return True
        i += 1

    return False
    
print(is_missing_char(original_word, answer_word, input_char))

