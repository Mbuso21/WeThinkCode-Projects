import tkinter
import turtle
from world import obstacles as ob

# Command section

def turtle_do_forward(robot, steps):
    '''
    moves turtle forward
    '''

    robot.fd(steps)


def turtle_do_backwards(robot, steps):
    '''
    moves turtle back
    '''

    robot.bk(steps)


def print_movement(robot_name, command_name, steps):
    '''
    Prints out the movement of the bot, forward or back
    '''
    print(f' > {robot_name} moved {command_name} by {str(steps)} steps.')


def turn_left_turtle(robot):
    '''
    turns turlte left
    '''

    robot.lt(90)


def turn_right_turtle(robot):
    '''
    turns turtle right
    '''

    robot.rt(90)


def turn_print(robot_name, command_name):
    '''
    Prints the movement left or right
    '''

    print(f'  > {robot_name} turned {command_name}.')


def replay_turtle_commands(robot_name, history, silent):
    '''
    Takes robot_name(str), history(list) and silent(bool)
    replays commands
    returns None
    '''

    for command in history:
        #print(command)
        turtle_handle_command(robot_name, command, history, silent)

    
    if not silent:
        print(f' > {robot_name} replayed {str(len(history))} commands')


def replay_silent_turtle(robot_name, history, silent):
    '''
    Takes robot_name(str), history(list) and silent(bool)
    switches the silent switch to true and calls replay_turtle_commands(robot_name, history, silent)
    returns None
    '''

    silent = True
    replay_turtle_commands(robot_name, history, silent) 
    print(f' > {robot_name} replayed {str(len(history))} commands silently')


def get_history_turtle(command, history):
    '''
    Takes command(str) and history(list) as param
    Appends commands and directions only
    returns updated history list
    '''

    history.append(command)
    history = list(filter(lambda comm: comm != 'help', history))
    history = [word for word in history if not 'replay' in word]
    return history

# Check out of bounds and obsticles section

def print_out_of_bounds(robot_name):
    '''
    prints the robot is out of bounds
    '''
    print(f'{robot_name}: Sorry, I cannot go outside my safe zone.')


def check_out_of_bounds(steps, robot):
    '''
    varifies if the robot is going out of bounds
    '''
    position = [pos for pos in robot.pos()]
    if position[0] + steps > 100 or position[0] + steps < -100 or position[1] + steps > 200 or position[1] + steps < -200:
        return False
    else:
        return True


def check_robot_obstacles_path(robot, steps, obstacles, command_name):
    '''
    Function checks whether the turtle has an obstacle in its way
    Param 1: turtle alias, robot
    Param 2: steps(int) taken by turtle
    Param 3: obstacles list
    Param 4: command_name(str) given to the robot

    Returns True is there is an obstacle between the robot and it destination

    Else returns True

    '''
    
    test_bot = robot.clone()
    test_bot.hideturtle()
    if command_name == 'forward':
        test_bot.fd(steps)
    if command_name == 'back':
        test_bot.bk(steps)
    
    start_x, start_y = [int(i) for i in robot.pos()]
    end_x, end_y = [int(i) for i in test_bot.pos()]

    if ob.is_path_blocked(start_x, start_y, end_x, end_y):
        test_bot.hideturtle()
        return True

    test_bot.hideturtle()    
    return False

# Drawing section

def draw_border(robot, robot_name):
    '''
    Function takes robot(turtle class) and draws a border in red
    '''

    screen_robot = turtle.Screen()
    screen_robot.title(robot_name)
    screen_robot.setup(300, 500)
    robot.speed(5)
    robot.penup()       # To switch off the pen
    robot.goto(100, 0)
    robot.pencolor('red')
    robot.pensize(5)  # Goes to the end of the boundery
    robot.pendown()     # To switch the pen on
    robot.rt(90)        
    robot.fd(200)       
    robot.rt(90)
    robot.fd(200)
    robot.rt(90)
    robot.fd(400)
    robot.rt(90)
    robot.fd(200)
    robot.rt(90)
    robot.fd(200)
    robot.penup()
    robot.home()

    obstacle = draw_obsticles(robot)
    return obstacle


def draw_obsticles(robot):
    '''
    Takes robot(Type: turtle class) and draws box obsticles on draw_border()
    '''

    robot.color('red')
    robot.pensize(1)
    robot.fillcolor('red')
    obstacles = ob.obstacles
    for postion in obstacles:
        robot.begin_fill()
        for xycor in postion[0:4]:
            robot.goto(xycor)
            robot.pendown()
        robot.goto(postion[0])
        robot.end_fill()
        robot.penup()
        
        robot.home()

    robot.color('black', 'red')
    robot.lt(90)
    return obstacles


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    return: (command, argument)
    """
    command.lower()
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def turtle_call_commands(robot, robot_name, command_name, steps, silent, command, history, obstacles):
    '''
    This function only calls the commands and returns a bool

    this function is called in the main robot module and switches the robot off
    '''

    if command_name == 'off':
        return False

    if command_name == 'forward':
        if check_robot_obstacles_path(robot, steps, obstacles,command_name):
            print(f' > {robot_name}: Sorry, there is an obstacle in the way.')
            return True

        if check_out_of_bounds(steps, robot):
            turtle_do_forward(robot, steps)
            if not silent:
                print_movement(robot_name, command_name, steps)
            return True
        else:
            print_out_of_bounds(robot_name)
            return True

    if command_name == 'back':
        if check_robot_obstacles_path(robot, steps, obstacles,command_name):
            print(f' > {robot_name}: Sorry, there is an obstacle in the way.')
            return True

        if check_out_of_bounds(steps, robot):
            turtle_do_backwards(robot, steps)
            if not silent:
                print_movement(robot_name, command_name, steps)
    
            return True
        else:
            print_out_of_bounds(robot_name)
            return True

    if command_name == 'left':
        turn_left_turtle(robot)
        if not silent:
            turn_print(robot_name, command_name)
        return True

    if command_name == 'right':
        turn_right_turtle(robot)
        if not silent:
            turn_print(robot_name, command_name)
        return True

    if command_name == 'replay':
        if command == 'replay silent':
            replay_silent_turtle(robot_name, history, silent)
            silent = False
            return True

        replay_turtle_commands(robot_name, history, silent)
        return True
    else:
        return True


def turtle_handle_command(robot_name, command, history, silent, obstacles):
    '''
    Takes robot_name(str) and command(str) as paramiters
    controls the robot according to the command and displays the command
    returns boolean whether the robot should ask for another instruction

    '''
    
    # Splits the command into command_name and int
    command_name, steps = split_command_input(command)
    try:
        steps = int(steps)
    except:
        None
    
    # Initailises the robot to the turtle pen
    robot = turtle

    return turtle_call_commands(robot, robot_name, command_name, steps, silent, command, history, obstacles)
