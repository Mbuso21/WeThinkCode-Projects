import random
# the belowe lambda is for testing to make it easier to see
# random.randint = lambda a, b:1

global obstacles

def is_position_blocked(x,y):
    '''
    Function Description:
        
        Function tests if x,y coordinates are in an obstacle
        Output will determine if the robot is at an obstacle
        Used in is_path_blocked()
        Param 1 and 2: x,y which is robot position
        
        returns True if position (x,y) falls inside an obstacle otherwise False
    '''
    global obstacles

    axis = (x, y)
    for box in obstacles:
        for position in box:
            if axis == position:
                return True

    return False


def is_path_blocked(x1,y1, x2, y2):
    '''
    Function Description:

        Checks to see if coordinates x1, y1 are in the path of an obstacle
        Param: x1,y1 as coordinates of the robot and x2, y2 as coordinates of robot destination
        returns True if there is an obstacle in the line between the coordinates (x1, y1) and (x2, y2).
    
        else returns False
    '''

    if x1 == x2:
        if y1 < y2:
            steps = y2 - y1
            x, y = x1, y1
            for i in range(steps):
                y += 1
                if is_position_blocked(x, y):
                    return True
            
        if y1 > y2:
            steps = y1 - y2
            x, y = x1, y1
            for i in range(steps, 0, -1):
                y -= 1
                if is_position_blocked(x, y):
                    return True
                
    if y1 == y2:
        if x1 < x2:
            steps = x2 - x1
            x, y = x1, y1
            for i in range(steps):
                x += 1
                if is_position_blocked(x, y):
                    return True  

        if x1 > x2:
            steps = x1 - x2
            x, y = x1, y1
            for i in range(steps, 0, -1):
                x -= 1
                if is_position_blocked(x, y):
                    return True
                
    return False


def get_obstacles():
    '''
    returns a random(1 to 10) list of obsticles for the toy_robot
    ''' 
    obstacles = []
    number_of_obstacles = random.randint(1, 10)
    for obs in range(number_of_obstacles):
        x = random.randint(-100, 100)
        y = random.randint(-200, 200)
        obstacles.append([(x,y), (x+4,y), (x+4,y+4), (x,y+4)])
    
    return obstacles


def get_obstacles_coordinates(obstacles):
    obstacles_all_coor = obstacles
    

    for i in obstacles_all_coor:
        
        for x in i:

            a = 1
            for count_x in range(3):
                i.append((x[0] + a, x[1]))
                a += 1 
            a = 1   
            for count_y in range(3):
                i.append((x[0] + 4, x[1] + a))
                a += 1
            a -= 1
            for count_x in range(3):
                i.append((x[0] + a, x[1] + 4))
                a -= 1
            a = 3
            for count_y in range(3):
                i.append((x[0], x[1] + a))
                a -= 1
            break
                   
        
    return obstacles_all_coor


def print_obstacles_position():
    '''
    Prints out the obstacles positions
    '''
    global obstacles

    obstacles = get_obstacles_coordinates(get_obstacles())

    if(len(obstacles)):
        print('There are some obstacles:')
        for lists in obstacles:
            print(f'- At position {lists[0][0]},{lists[0][1]} (to {lists[2][0]},{lists[2][1]})')
    

