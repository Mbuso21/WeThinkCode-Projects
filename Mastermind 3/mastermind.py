import random

# code = [0, 0, 0, 0]
# correct_digits_and_position = 0
# correct_digits_only = 0
# correct = False


def create_code():
    """Function that creates the 4 digit code, using random digits from 1 to 8"""

    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    
    #print(code)
    return code


def show_instructions():
    """Shows instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(correct_digits_and_position, correct_digits_only):
    """Show the results from one turn"""

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))


def take_turn(code):
    """Handle the logic of taking a turn, which includes:
       * get answer from user
       * check if answer is valid
       * check correctness of answer
       * returns a tuple
    """

    correct_digits_and_position = 0
    correct_digits_only = 0

    answer = get_answer_input()
    answer = list(answer)
    answer = [int(i) for i in answer]
    for i in range(len(answer)):
        if code[i] == (answer[i]):
            correct_digits_and_position += 1
        elif answer[i] in code:
            correct_digits_only += 1

    show_results(correct_digits_and_position, correct_digits_only)

    return correct_digits_and_position, correct_digits_only

def get_answer_input():
    ask_again = True
    while ask_again:
        try:
            code_breaker = int(input('Input 4 digit code: '))                   # takes input and converts to int
            code_breaker = list(str(code_breaker))                              # takes input and converts to a string since you you cant iterate an int  
            if len(code_breaker) > 4 or len(code_breaker) <  4:                 #compares if length is the greater than or less than the code
                ask_again = True                                                #if true assigns True to ask_again                                           
                print("Please enter exactly 4 digits.")
            else:
                ask_again = False
        except ValueError:
            print("Please enter exactly 4 digits.")
            ask_again = True
    
    #code_breaker = [int(i) for i in code_breaker]
    code_breaker = ''.join(code_breaker)

    return code_breaker

    # valid_entry = False
    # while not valid_entry:

    #         try:
    #             answer = int(input("Input 4 digit code: "))
    #             invald_entry = True
    #             answer = str(answer)
    #             while len(answer) < 4 or len(answer) > 4:
    #                 print("Please enter exactly 4 digits.")
    #                 answer = input("Input 4 digit code: ")
    #                 valid_entry = answer.isdigit()
    #         except ValueError:
    #             valid_entry = False
        
    # while len(answer) < 4 or len(answer) > 4:
    #     print("Please enter exactly 4 digits.")
    #     answer = input("Input 4 digit code: ")
    
    #return answer

def show_code(code):
    """Show Code that was created to user"""

    print('The code was: '+str(code))


def check_correctness(turns, correct_digits_and_position):
    """Checks correctness of answer and show output to user"""

    #global correct

    if correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        
    return False

def run_game():
    """Main function for running the game"""

    #global correct
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        #print(code)
        correct_digits_and_position = take_turn(code)
        turns += 1
        #print(correct_digits_and_position[0])
        correct = check_correctness(turns, correct_digits_and_position[0])
        #print(correct)

    show_code(code)


if __name__ == "__main__":
    run_game()
