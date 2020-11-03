import word_processor
import sys
import unittest
from io import StringIO

class MyTestCase(unittest.TestCase):

    def test_if_convert_to_word_returns_a_list(self):
        self.assertIsInstance(word_processor.convert_to_word_list('Hello, my name is mbuso, whats yours?'), list)

    
    def test_if_convert_to_word_returns_list_of_words_and_lowercase(self):
        self.assertEqual(['hello', 'my', 'name', 'is', 'mbuso', 'whats', 'yours'], word_processor.convert_to_word_list('Hello, my name is mbuso, whats yours?'))

    
    def test_if_convert_to_word_returns_an_empty_list_when_string_is_(self):
        self.assertEqual([], word_processor.convert_to_word_list(''))


    def test_words_longer_than5(self):
        self.assertEqual(['mehlomakulu'], word_processor.words_longer_than(5, 'Hello, my name is mbuso Mehlomakulu, whats yours?'))

    
    def test_words_longer_than_returns_list(self):
        self.assertIsInstance(word_processor.words_longer_than(5, ''), list)


    def test_words_length_map_returns_dict(self):
        self.assertIsInstance(word_processor.words_lengths_map('Hello, my name is mbuso Mehlomakulu, whats yours?'), dict)

    
    def test_words_length_map_works(self):
        self.assertEqual({2:2,4:1,5:4,11:1}, word_processor.words_lengths_map('Hello, my name is mbuso Mehlomakulu, whats yours?'))


    def test_letters_count_map_returns_dict(self):
        self.assertIsInstance(word_processor.letters_count_map('Hello, my name is mbuso Mehlomakulu, whats yours?'), dict)


    def test_letters_count_map_workd(self):
        self.assertEqual({'a': 3, 'b': 1, 'c': 0, 'd': 0, 'e': 3, 'f': 0, 'g': 0, 'h': 3, 'i': 1, 'j': 0, 'k': 1, 'l': 4, 'm': 5, 'n': 1, 'o': 4, 'p': 0, 'q': 0, 'r': 1, 's': 4, 't': 1, 'u': 4, 'v': 0, 'w': 1, 'x': 0, 'y': 2, 'z': 0}, word_processor.letters_count_map('Hello, my name is mbuso Mehlomakulu, whats yours?'))

    def test_most_used_character_returns_a_string_len1(self):
        self.assertEqual(1,len(word_processor.most_used_character('Hello, my name is mbuso Mehlomakulu, whats yours?')))

    def test_most_used_character_returns_a_string(self):
        self.assertIsInstance(word_processor.most_used_character('Hello, my name is mbuso Mehlomakulu, whats yours?'), str)
    
    def test_most_used_character_returns_empty_list(self):
        self.assertEqual(None, word_processor.most_used_character(''))

    def test_most_used_character_digit_returns_empty_list(self):
        self.assertEqual(None, word_processor.most_used_character('1234'))

if __name__ == "__main__":
    unittest.main()
        