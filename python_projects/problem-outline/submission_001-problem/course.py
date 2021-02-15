import random

def create_outline():
    """
    TODO: implement your code here
    """

    #Step 1 

    print('Course Topics:')
    course_outline = set([
        'Introduction to Python', 
        'Tools of the Trade', 
        'How to make decisions', 
        'How to repeat code', 
        'How to structure data',
        'Functions',
        'Modules'])

    #step 4 and Step 1
    course_outline = list(course_outline)
    course_outline.sort()
    for word in course_outline:
        print('* ' + word) 
    print()

    #Step 2
    problems = ['Problem 1', 'Problem 2', 'Problem 3']
    problems_str = ', '.join(problems)

    course_dict = dict.fromkeys(course_outline, problems_str)

    print("Problems: ")
    for word in course_dict:
        print('* ' + word + ' : ' + course_dict[word])

    #Step 3
    
    student_name = [
        'Nyari',
        'Adam',
        'Sipho',
    ]

    status = ['[STARTED]', '[GRADED]', '[COMPLETED]']
    x = 0
    student_tuple_list = [(student_name[x], course_outline[x], problems[x], status[x])]
    x += 1
    for y in range(len(student_name) - 1):
        student_tuple_list.insert(x, (student_name[x], course_outline[x], problems[x], status[x]))
        x += 1
    print()
    print(student_tuple_list)
    print()

    print('Student Progress:')
    i = 1
    for student in range(len(student_name)):
        print(f'{i}.  {student_tuple_list[student][0]} - {student_tuple_list[student][1]} - {student_tuple_list[student][2]} {student_tuple_list[student][3]}')
        i += 1

if __name__ == "__main__":
    create_outline()
