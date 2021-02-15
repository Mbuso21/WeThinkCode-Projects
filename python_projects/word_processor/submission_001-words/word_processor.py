from string import *


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    '''
    Converts text entered in a sentence into a list of words

    returns a list 
    '''
    delimiters = ',.?!;: '

    convert = split(delimiters, text)
    convert = [word.lower() for word in convert]
    convert = [word for word in convert if word != '']

    return convert


def words_longer_than(length, text):
    '''
    Takes in an int leangth and str text and returns words that are longer than the length int

    returns a list of words longer than the length
    '''
    convert = convert_to_word_list(text)
    longer_than = list(filter(lambda word: len(word) > length, convert))
    #return [word for word in covert if word > length]
    return longer_than


def words_lengths_map(text):
    '''
    takes a text sentence

    returns a dict with the keys being the len(word) and value being the amount of times it occures.
    '''
    convert = convert_to_word_list(text)
    lengths = [len(word) for word in convert]
    lengths.sort()
    return {key:lengths.count(key) for key in lengths}


def letters_count_map(text):
    '''
    take in a text and returns a dict of keys alphabet, value the number of times than letter appears in the text
    '''

    alphabet = ascii_lowercase
    convert = convert_to_word_list(text)
    convert = ''.join(convert)
    return {key:convert.count(key) for key in alphabet}


def most_used_character(text):
    '''
    takes text input and returns one character which is the most used one
    '''
    if text.isdigit() or text == '':
        return None
    inverse_letters_map = {}
    letters_map = letters_count_map(text)
    values = letters_map.values()
    max_values = max(values)
    inverse_letters_map = {value:key for (key,value) in letters_map.items()}
    return inverse_letters_map[max_values]