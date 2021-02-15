# element = [7,5,2,4]
def find_min(element):
    """
    Function Description:

        * Returns the min value in a list like min()
        * find_min(list)
        * all elements in the list must be int otherwise returns -1
    """
    if any(isinstance(i,str) for i in element) or len(element) == 0 or any(isinstance(i,float) for i in element):
        return -1
    if len(element) == 1:
        return element[0]
    small_value  = element[0]
    min_value = find_min(element[1:])

    if small_value < min_value:
        return small_value
    else:
        return min_value
        

def sum_all(element):
    """
    Function Description:

        * sum_all(list)
        * Returns a list with the total added value
        * Takes a list element in parathesis
        * All values in the list must be int otherwise returns -1
    """
    if any(isinstance(i,str) for i in element) or len(element) == 0 or any(isinstance(i,float) for i in element):
        return -1
    if len(element) == 1:
        return element[0]
    else:
        return element[0] + sum_all(element[1:])


def find_possible_strings(character_set, n):
    """
    Function Description:

        * find_possible_strings(list, int)
        * Returns combination of char list and number n
        * Takes list and int in parathesis
        * All vaules in the list must be str otherwise returns []
        * Calls an addition fuction which then recurses
    """
    if any(isinstance(i,int) for i in character_set) or any(i.isdigit() for i in character_set) or any(i == '' for i in character_set) or any(character_set) == False:
        return []
    if len(character_set) == 1:
        for i in range(n - 1):
            character_set.append(character_set[0])
        return character_set
    result_set = []
    set_len = len(character_set)
    find_possible_strings_rec(character_set, '', set_len, n, result_set)
    return result_set

def find_possible_strings_rec(character_set, prefix, set_len, n, result_set):
    '''
    Recursive function of find_possible_strings(str, int)
    '''

    if (n == 0):
        #print(prefix)
        result_set.append(prefix)
        return

    for i in range(set_len):
        new_prefix = prefix + character_set[i]
        find_possible_strings_rec(character_set, new_prefix, set_len, n - 1, result_set)



# if __name__ == '__main__':
   
    # element = [7,5,2,1]

    # print(find_min(element))

    # print(sum_all(element))

    # a = ['a']

    # print(find_possible_strings(a,5))
    # print(i for i in find_possible_strings(a, 5)) 
