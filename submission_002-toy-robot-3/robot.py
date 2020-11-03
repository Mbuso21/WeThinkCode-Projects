from io import StringIO
import sys

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay', 'replay silent', 'replay reversed', 'replay reversed silent', '-', ]
single = ['silent', 'reversed', 'replay']

history_list = []

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

# To enable the all the silent 
silent = False

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def capture_io():
    ''' This helps us not repeat the below function in the test_robot.py'''

    text_capture = StringIO()
    sys.stdout = text_capture

    return text_capture


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    #print(command)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """



    # Test if user enters replay 0
    if 'replay' in command.lower() and any(i == '0' for i in command.lower()):
        return False

    # Tests if user enters replay commands with silent and reversed
    if command.lower() == 'replay silent' or command.lower() == 'replay reversed' or command.lower() == 'replay reversed silent' or '-' in command.lower() or command.lower() == 'replay':
        if 'replay' in command.lower() and '-' in command:
            #Tests step 6.2
            command_split = command.split(' ')
            argtest = command_split[1].split('-')
            try:
                argtest = [int(i) for i in argtest]
                return True
            except:
                return False
        else:
            return True

    # Test step 6.3 in the tests
    if command.split(' ')[0] == 'replay':
        num = ''
        test_command = command.split(' ')
        steps = list(filter(lambda word: word.isdigit(),test_command))
        num = ''.join(steps)
        
        try:
            test_command.remove(num)
        except ValueError:
            return False

        if all(word in single for word in test_command):
            return True
        else:
            return False
    
    
    # Splits the command into an element of two
    (command_name, arg1) = split_command_input(command)
    # print(command_name)
    # print(arg1)

    #Tests replay 0 again incase it slips the top one
    if arg1 == '0' and command_name.lower() == 'replay':
        return False

    return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replay previous commands
REPLAY SILENT - replays previous commands with no steps
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def do_replay(robot_name, history_list):
    '''
    Function takes robot_name(str) and history_list(list) as params
    replays previous commands by calling the handle_command()

    returns a boolean value
    '''
    do_next = True
    for command in history_list:
        do_next = handle_command(robot_name, command, history_list)
    
    print(f' > {robot_name} replayed {str(len(history_list))} commands.',end='')

    return do_next


def do_replay_silent(robot_name, history_list):
    '''
    Function takes robot_name(str) and history_list(list) as params
    replays previous commands by calling the handle_command() and doesn't display the commands

    returns a boolean value and the silent switch that turns display on/off
    '''
    do_next = True
    for command in history_list:
        do_next = handle_command(robot_name, command, history_list)
    
    print(f' > {robot_name} replayed {str(len(history_list))} commands silently.')

    show_position(robot_name)
    silent = False

    return do_next, silent  


def do_replay_reversed(robot_name, history_list):
    '''
    Function takes robot_name(str) and history_list(list) as params
    replays previous commands in REVERSE by calling the handle_command()

    returns a boolean value
    '''

    do_next = True
    for command in history_list[::-1]:
        do_next = handle_command(robot_name, command, history_list)
    
    print(f' > {robot_name} replayed {str(len(history_list))} commands in reverse.',end='')

    return do_next


def do_replay_reversed_silent(robot_name, history_list):
    '''
    Function takes robot_name(str) and history_list(list) as params
    replays previous commands in REVERSE by calling the handle_command() and doesn't display the commands

    returns a boolean value and the silent switch that turns display on/off
    '''

    do_next = True
    for command in history_list[::-1]:
        do_next = handle_command(robot_name, command, history_list)
    
    print(f' > {robot_name} replayed {str(len(history_list))} commands in reverse silently.')

    show_position(robot_name)
    silent = False

    return do_next, silent


def do_replay_limit(robot_name, history_list, arg):
    '''
    Function takes robot_name(str), history_list(list) and arg(int) as params
        replays the last (arg) commands and call do replay with reduced list

    returns a boolean value
    '''
    
    limit_history = history_list[-arg:]
    #print(limit_history)
    do_next = do_replay(robot_name, limit_history)
    #print(f' > {robot_name} replayed {str(len(history_list))} commands.',end='')

    return do_next


def do_replay_range(robot_name, history_list, arg):
    '''
    Function takes robot_name(str), history_list(list) and arg(list) as params
        replays the last arg[1] to arg[0] commands and calls do replay with reduced list

    returns a boolean value
    '''

    arg = [i - 1 for i in arg]
    range_history = history_list[arg[1]:arg[0]]
    do_next = do_replay(robot_name, range_history)

    return do_next


def do_replay_limit_silent(robot_name, history_list, arg):
    '''
    Function takes robot_name(str), History_list(list) and arg(int)

        limits the command history and passes the new history to the do_replay_reversed function.
        has a switch called silent and when true, doesnt print commands

        returns a tuple value to continue the prompts or not
    '''

    limit_history = history_list[-arg:]
    silent = True
    do_next, silent = do_replay_silent(robot_name, limit_history)
    silent = False
    return do_next, silent


def do_replay_limit_reversed(robot_name, history_list, arg):
    '''
    Function takes robot_name(str), History_list(list) and arg(int)

        limits the command history and passes the new history to the do_replay_reversed function.

        returns a boolean value to continue the prompts or not
    '''

    limit_history = history_list[:arg]
    do_next = do_replay_reversed(robot_name, limit_history)

    return do_next


def handle_command(robot_name, command, history_list):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    global silent
    command_output = ''
    command_name = ''
    do_next = ''

    (command_name, arg) = split_command_input(command)
    
    if command_name == 'off':
        return False

    if command_name == 'help':
        (do_next, command_output) = do_help()

    if command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg))

    if command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg))

    if command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)

    if command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)

    if command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg))

    if command == 'replay':
        do_next = do_replay(robot_name, history_list)

    if command == 'replay silent':
        silent = True
        do_next, silent = do_replay_silent(robot_name, history_list)
        silent = False

    if command == 'replay reversed':
        do_next = do_replay_reversed(robot_name, history_list)

    if command == 'replay reversed silent':
        silent = True
        do_next, silent = do_replay_reversed_silent(robot_name, history_list)
        silent = False

    if command_name == 'replay' and arg.isdigit():
        do_next = do_replay_limit(robot_name, history_list, int(arg))
    
    #Step 6.2
    if 'replay' in command and '-' in command:
        command_name, arg = split_command_input(command)
        arg = arg.split('-')
        arg = [int(i) for i in arg]
        if arg[0] < arg[1] or arg[0] == arg[1]:
            do_next, command_output = do_forward(robot_name, 0)
        else:
            do_next = do_replay_range(robot_name,history_list,arg)
    
    # step 6.3 replay 2 silent and replay 2 reversed
    if len(command.split(' ')) == 3 and any(word.isdigit() for word in command.split()):
        command_split_3 = command.split(' ')
        int_in_command = [word for word in command_split_3 if word.isdigit()]
        arg = int(int_in_command[0])
        if any(word == 'silent' for word in command_split_3):    
            silent = True
            do_next, silent = do_replay_limit_silent(robot_name, history_list, arg)
            silent = False
        if any(word == 'reversed' for word in command_split_3):
            do_next = do_replay_limit_reversed(robot_name, history_list, arg)


    if not silent and command != 'replay silent' and 'silent' not in command:
        if command != 'replay reversed silent':
            
            print(command_output)
            show_position(robot_name)
    return do_next


def command_history(command, history_list): 
    '''
    Saves the command history in a list
     param 1: command str
     param 2: list that keeps saving the commands: 'forward, back,left, right only
     returns: history_list
    '''
    history_list.append(command)

    history_list = list(filter(lambda comm: comm != 'help', history_list))
    history_list = [word for word in history_list if not 'replay' in word]
    #print(history_list)

    return history_list
    

def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history_list
    
    position_x = 0
    position_y = 0
    current_direction_index = 0
    history_list = []
    
    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")

    command = get_command(robot_name)
    history_list = command_history(command, history_list)
    while handle_command(robot_name, command, history_list):
        command = get_command(robot_name)
        history_list = command_history(command, history_list)

    history_list = []
    output(robot_name, "Shutting down..")



if __name__ == "__main__":
    robot_start()