import random
#from display_char import random_fill_word

original_word = 'feet'
answer_word = '__e_' #random_fill_word(original_word)

count = len(answer_word)
index = 0
global ran_index
ran_index = 0

while count > 0:
    if answer_word[index] != '_':
        ran_index = index
    
    count -= 1
    index += 1

    

char_list = 'abcdefghijklmnop'
input_char =  input('Enter letter: ') #random.choice(char_list)

print('original_word: ' + original_word)
print('Input_char: ' + input_char)
print('answer_word: ' + answer_word)
print('ran_index: ' + str(ran_index))


def is_missing_char(original_word, answer_word, char):
    if char in original_word and char in answer_word and char != original_word[ran_index]:
        return True
    else:
        return False


print(is_missing_char(original_word, answer_word, input_char))

