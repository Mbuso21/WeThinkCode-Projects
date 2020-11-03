import sys
from io import StringIO
from world.text.world import update_position
import world.obstacles as ob
import world.text.world as worldly
if len(sys.argv) > 1:
    if sys.argv[1] == 'turtle':
        import world.turtle.world as turtle_world
        import turtle
    





"""
TODO: You can either work from this skeleton, or you can build on your solution for Toy Robot 3 exercise.
"""

# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint']
move_commands = valid_commands[3:]


history = []


def capture_io():
    '''This helps us not repeat the below function in the test_robot.py'''

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
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    command.lower()
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

    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed','').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed','')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    else:
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
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""

def get_commands_history(reverse, relativeStart, relativeEnd):
    """
    Retrieve the commands from history list, already breaking them up into (command_name, arguments) tuples
    :param reverse: if True, then reverse the list
    :param relativeStart: the start index relative to the end position of command, e.g. -5 means from index len(commands)-5; None means from beginning
    :param relativeEnd: the start index relative to the end position of command, e.g. -1 means from index len(commands)-1; None means to the end
    :return: return list of (command_name, arguments) tuples
    """

    commands_to_replay = [(name, args) for (name, args) in list(map(lambda command: split_command_input(command), history)) if name in move_commands]
    if reverse:
        commands_to_replay.reverse()

    range_start = len(commands_to_replay) + relativeStart if (relativeStart is not None and (len(commands_to_replay) + relativeStart) >= 0) else 0
    range_end = len(commands_to_replay) + relativeEnd if  (relativeEnd is not None and (len(commands_to_replay) + relativeEnd) >= 0 and relativeEnd > relativeStart) else len(commands_to_replay)
    return commands_to_replay[range_start:range_end]


def do_replay(robot_name, arguments):
    """
    Replays historic commands
    :param robot_name:
    :param arguments a string containing arguments for the replay command
    :return: True, output string
    """

    silent = arguments.lower().find('silent') > -1
    reverse = arguments.lower().find('reversed') > -1
    range_args = arguments.lower().replace('silent', '').replace('reversed', '')

    range_start = None
    range_end = None

    if len(range_args.strip()) > 0:
        if is_int(range_args):
            range_start = -int(range_args)
        else:
            range_args = range_args.split('-')
            range_start = -int(range_args[0])
            range_end = -int(range_args[1])

    commands_to_replay = get_commands_history(reverse, range_start, range_end)

    for (command_name, command_arg) in commands_to_replay:
        (do_next, command_output) = call_command(command_name, command_arg, robot_name)
        if not silent:
            print(command_output)
            worldly.show_position(robot_name)

    return True, ' > '+robot_name+' replayed ' + str(len(commands_to_replay)) + ' commands' + (' in reverse' if reverse else '') + (' silently.' if silent else '.')


def call_command(command_name, command_arg, robot_name):
    '''
    Calls the commands
    '''

    if command_name == 'help':
        return do_help()
    elif command_name == 'forward':
        return worldly.do_forward(robot_name, int(command_arg))
    elif command_name == 'back':
        return worldly.do_back(robot_name, int(command_arg))
    elif command_name == 'right':
        return worldly.do_right_turn(robot_name)
    elif command_name == 'left':
        return worldly.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return worldly.do_sprint(robot_name, int(command_arg))
    elif command_name == 'replay':
        return do_replay(robot_name, command_arg)
    return False, None


def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        history.clear()

        return False
    else:
        (do_next, command_output) = call_command(command_name, arg, robot_name)

    print(command_output)
    worldly.show_position(robot_name)
    add_to_history(command)
    #print(history)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    
    history.append(command)
    #print(history)


def robot_start():
    """This is the entry point for starting my robot"""

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    ob.print_obstacles_position()
    worldly.position_x = 0
    worldly.position_y = 0
    worldly.current_direction_index = 0
    history = []
    silent = False

    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'turtle':
            bot = turtle
            obstacles = turtle_world.draw_border(bot, robot_name)
            command = get_command(robot_name)
            history = turtle_world.get_history_turtle(command, history)
            while turtle_world.turtle_handle_command(robot_name, command, history, silent, obstacles):
                command = get_command(robot_name)
                history = turtle_world.get_history_turtle(command, history)
        else:
            command = get_command(robot_name)
            while handle_command(robot_name, command):
                command = get_command(robot_name)
    else:
        command = get_command(robot_name)
        while handle_command(robot_name, command):
            command = get_command(robot_name)

    history.clear()
    # ob.obstacles.clear()

    output(robot_name, "Shutting down..")
    

if __name__ == "__main__":
    robot_start()
    # help("modules")
    
   