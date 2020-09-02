

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():

    shape = input('Shape?: ')
    shape = shape.lower()

    while shape != 'pyramid' and shape != 'square' and shape != 'triangle' and shape != 'rectangle' and shape != 'diamond' and shape != 'parallelogram' and shape != 'rhombus':
        shape = input('Shape?: ')
        shape = shape.lower()

    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():

    height_param = input('Height?: ')
    is_int = height_param.isdigit()

    while is_int == False or int(height_param) > 80:
        height_param = input('Height?: ')
        is_int = height_param.isdigit()

    return int(height_param)

# TODO: Step 2
def draw_pyramid(height, outline):

    if outline == False:
        rows = 1
        count = height
        height -= 1
        while count > 0:
            print(" " * height + "*" * rows)
            height -= 1
            rows += 2
            count -= 1
    else:
        space = height
        space -= 1
        rows = 1
        print(" "* space + "*")
        space -= 1
        while space > 0:
            print(" " * space + "*" + " " * rows + "*")
            space -= 1
            rows += 2
        rows += 2
        print("*" * rows)

# TODO: Step 3
def draw_square(height, outline):
    
    if outline == False:
        rows = height
        while height > 0:
            print("*" * rows)
            height -= 1
    else:
        space = height -2
        index = space
        print("*" * height)
        while index > 0:
            print("*" + " " * space + "*")
            index -= 1
        print("*" * height)

# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        rows = 1
        while height > 0:
            print("*" * rows)
            height -= 1
            rows += 1

    else:
        base = height
        height -= 2
        space = 0
        print("*")
        while height > 0:
            print("*" + " " * space + "*")
            height -= 1
            space += 1
        print("*" * base)


# TODO: Steps 2 to 4, 6 - add support for other shapes

def draw_rectangle(height, outline):
    if outline == False:

        rows = height * 5
        while height > 0:
            print("*" * rows)
            height -= 1
    else:

        height_inner = height - 2
        rows = height * 5
        spaces = rows - 2
        print("*" * rows)
        while height_inner > 0:
            print("*" + " " * spaces + "*")
            height_inner -= 1
        print("*" * rows)

def draw_diamond(height, outline):

    mod = height % 2
    while mod == 0:
        height = input('A diamond cannot have an even height, enter height again: ')
        mod = int(height) % 2
    
    height = int(height)

    if outline == False:

        height = int(height/2) + (int(height) % 2) - 1
        index = height
        rows = 1
        while index > 0:
            print(" "* index + "*" * rows)
            index -= 1
            rows += 2

        while index < height:
            print(" " * index + "*" *rows)
            index += 1
            rows -= 2

        print(" " * height+ "*")
    else:

        height = int(height/2) + (height % 2) - 1
        space = height
        space -= 1
        rows = 1
        print(" "* height + "*")
        while space > 0:
            print(" " * space + "*" + " " * rows + "*")
            space -= 1
            rows += 2

        while space < height:
            print(" " * space + "*" + " " * rows + "*")
            space += 1
            rows -= 2

        print(" "* height + "*")

def draw_parallelogram(height, outline):

    if outline == False:
        rows =  height * 4
        while height > 0:
            print(' ' * height + "*" * rows)
            height -= 1
    else:
        rows = height * 4
        space1 = height - 1
        print(' ' * space1 + "*" * rows)
        index = height - 2
        spaces = rows - 2
        while index > 0:
            print(' ' * index + '*' + ' ' * spaces + '*')
            index -= 1
        print(' ' * index + "*" * rows)

def draw_rhombus(height, outline):

    if outline == False:
        rows =  height
        while height > 0:
            print(' ' * height + "*" * rows)
            height -= 1
    
    else:
        rows = height
        space1 = height - 1
        print(' ' * space1 + "*" * rows)
        index = height - 2
        spaces = rows - 2
        while index > 0:
            print(' ' * index + '*' + ' ' * spaces + '*')
            index -= 1
        print(' ' * index + "*" * rows)

def draw(shape, height, outline):
    if shape == 'triangle':

        draw_triangle(height, outline)

    if shape == 'pyramid':

        draw_pyramid(height, outline)
    
    if shape == 'square':

        draw_square(height, outline)
    
    if shape == 'rectangle':

        draw_rectangle(height, outline)
    
    if shape == 'diamond':
        draw_diamond(height, outline)
    
    if shape == 'parallelogram':
        draw_parallelogram(height, outline)
    
    if shape == 'rhombus':
        draw_rhombus(height, outline)
    
        


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():

    outline = input('Outline?(y/n): ').lower()

    while outline != '' and outline != 'y' and outline != 'n':
        outline = input('Outline?(y/n): ').lower()

    if outline == 'y':
        return True
    else:
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)
    


