

# TODO: Decompose into functions

def move_forward_turn_right(size, degrees):
    '''
    Summary or Description of the Function:
        
        Takes two parameters: size and degrees

        Prints out "Move Forward (size)"
        prints out "Turn Right (degrees)
        
        returns none
        '''

    print("* Move Forward "+str(size))
    print("* Turn Right "+str(degrees)+" degrees")


def move_square(size, degrees):
    '''
    Summary or Description of the Function:

        Commants a move in a square shape
        
        Takes two parameters: size and degrees
        
        Prints:"Moving in a square of (size)

        runs a for loop that iterates 4 times 
        
        Prints move_forward_turn_right(size, degrees) - use help(move_forward_turn_right)
        
        returns none
        '''
    print("Moving in a square of size "+str(size))
    for i in range(4):
        move_forward_turn_right(size, degrees)

    
def move_rectangle():
    '''
    Summary or Description of the Function:

        Command to move in a rectangular shape

        Takes no paramiters

        init length = 20 and width = 10

        Prints: ""Moving in a rectangle of (length) by (width)"

        Uses for loop to iter 2 times

        init degrees = 90

        calls move_forward_turn_right(length, degrees)
        calls move_forward_turn_right(width, degrees)

        returns none
        
    '''
    length = 20
    width = 10
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        move_forward_turn_right(length, degrees)
        move_forward_turn_right(width, degrees)


def move_circle(length, degrees):
    '''
    Summary or Description of the Function:

        Commands to move in a circle shape

        Takes paramiters length and degress

        Init degrees = 1

        Uses for loop to iter 360 times

        Init length to 1

        uses move_forward_turn_right(length, degrees)
        
    '''
    print("Moving in a circle")
    degrees = 1
    for i in range(360):
        length = 1
        move_forward_turn_right(length, degrees)


def square_dance():
    '''
    Summary or Description of the Function:

        Commands to move in a square dance

        Takes no paramiters

        uses move_square(20, 90)

        returns none
    '''
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        length = 20
        print("* Move Forward "+str(length))
        move_square(20, 90)
            

def move_in_crop_circles():
    '''
    Summary or Description of the Function:
        
        Takes no paramiters

        Init length = 20

        Uses move_circle(1, 1)

        Returns none
    '''
    print("Crop circles - 4 circles")
    for i in range(4):
        length = 20
        print("* Move Forward "+str(length))
        move_circle(1, 1)


def move(): #Should be named move_robot
    '''Summary or Description of the Function:
        
        Takes other functions to run a move robot function
        
        You will move the robot by calling other functions into it'''

    move_square(10, 90)
    move_rectangle()
    move_circle(1,1)
    square_dance()
    move_in_crop_circles()
    



def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
    help(move_square)