import random

def generate_ran_code():
    '''
    Function Description:

        generates a random 4 didgit code that has no duplicates

        Takes no paramiters

        returns the code

    '''

    code = [0,0,0,0]
    for i in range(0,4):
        ran_int = random.randint(1,8)
        while ran_int == code[0] or ran_int == code[1] or ran_int == code[2] or ran_int == code[3]:
            ran_int = random.randint(1,8)
        code[i] = ran_int
    
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')

    return code

def user_input_code(code):
    '''
    Function Description:
        
        Makes sure that the input is len-4 and has no alpha chars

        Takes a list in paranthesis from generate_ran_code()

        returns the user in a int list
    '''

    ask_again = True
    while ask_again:
        try:
            code_breaker = int(input('Input 4 digit code: '))                   # takes input and converts to int
            code_breaker = list(str(code_breaker))                              # takes input and converts to a string since you you cant iterate an int  
            if len(code_breaker) > len(code) or len(code_breaker) <  len(code): #compares if length is the greater than or less than the code
                ask_again = True                                                #if true assigns True to ask_again                                           
                print("Please enter exactly 4 digits.")
            else:
                ask_again = False
        except ValueError:
            print("Please enter exactly 4 digits.")
            ask_again = True
    
    code_breaker = [int(i) for i in code_breaker]

    return code_breaker

def compare_user_answer_to_code(code_breaker, code):
    '''
    Function Description:

        Compares user input with randomly generated code and prints out the number of occurances

        Takes the user input as the code and takes the randomly generated code

        returns none
    '''
    global corr_num 
    corr_num = 0
    for index in range(len(code)):
        if code_breaker[index] == code[index]:
            corr_num += 1

    print(f'Number of correct digits in correct place:     {corr_num}')

    global corr_num2
    corr_num2 = 0
    for i in range(len(code)):
        if code_breaker[i] != code[i]:
            if code_breaker[i] in code:
                corr_num2 += 1
    
    print(f'Number of correct digits not in correct place: {corr_num2}')


def end_game(code):
    '''
    Function Description:
        
        Ends the game with a win if guessed correctly or a lose after 12 turns

        Takes a 4-digit code randomly generated code

        calls functions user_input_code(code) and compare_user_answer_to_code(code_breaker, code)

        Returns none
    '''
    guesses = 12
    while True:
        code_breaker = user_input_code(code)
        compare_user_answer_to_code(code_breaker, code)
        if corr_num == len(code):
                print('Congratulations! You are a codebreaker!')
                code = [str(i) for i in code]
                code = ''.join(code)
                print(f'The code was: {code}')
                break
        else:
            guesses -= 1
            print(f'Turns left: {guesses}') 

            if guesses == 0:
                print('Out of turns')
                code = [str(i) for i in code]
                code = ''.join(code)
                print(f'The code was: {code}')
                break

def print_code(code):
    print(code)

def run_game():
    '''
    Runs the game
    '''
    
    code = generate_ran_code()
#     print_code(code)
    end_game(code)   

    

if __name__ == "__main__":
    run_game()
    
