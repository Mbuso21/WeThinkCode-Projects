import random
from display_char import random_fill_word

original_word = 'feet'
answer_word = random_fill_word(original_word)

print(answer_word)

char_list = 'abcdefghijklmnop'
input_char =  input('Enter letter: ')

def is_missing_char(original_word, answer_word, char):
    i = 0
    for chara in original_word:
        if chara == char and  answer_word[i] == '_':
            return True
        i += 1

    return False
    
print(is_missing_char(original_word, answer_word, input_char))


def fill_in_char(original_word, answer_word, char):
    #if_true = is_missing_char(original_word, answer_word, input_char)
    #if if_true:
    i = 0
    for word in original_word:
        if word == char and answer_word[i] == '_':
            new_answer = list(answer_word)
            new_answer[i] = char
            new_list = ''.join(new_answer)
            return new_list
        i += 1
    return answer_word


print(fill_in_char(original_word, answer_word, input_char))