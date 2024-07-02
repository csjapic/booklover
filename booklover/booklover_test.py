import pandas as pd
import numpy as np
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        b1 = BookLover('Julia', 'jdw4py@virginia.edu', 'mystery')
        b1.add_book('The Hunger Games', 4)
        self.assertTrue(b1.has_read('The Hunger Games'))
        
    def test_2_add_book(self):
        b1 = BookLover('Julia', 'jdw4py@virginia.edu', 'mystery')
        b1.add_book('The Hunger Games', 4)
        b1.add_book('The Hunger Games', 4)
        self.assertEqual(b1.book_list[b1.book_list['book_name'] == 'The Hunger Games'].shape[0], 1) 
    
    def test_3_has_read(self):
        b1 = BookLover('Julia', 'jdw4py@virginia.edu', 'mystery')
        b1.add_book('The Hunger Games', 4)
        self.assertTrue(b1.has_read('The Hunger Games'))
        
    def test_4_has_read(self):
        b1 = BookLover('Julia', 'jdw4py@virginia.edu', 'mystery')
        self.assertFalse(b1.has_read('Harry Potter'))        
        
    def test_5_num_books_read(self):
        b1 = BookLover('Julia', 'jdw4py@virginia.edu', 'mystery')
        b1.add_book('The Hunger Games', 4)
        b1.add_book('Dracula', 2)
        b1.add_book('Twilight', 4)
        b1.add_book('The Alchemist', 3)
        print(b1.num_books)
        self.assertEqual(b1.num_books_read(), 4)
        
    def test_6_fav_books(self):
        b1 = BookLover('Julia', 'jdw4py@virginia.edu', 'mystery')
        b1.add_book('The Hunger Games', 4)
        b1.add_book('The Giver', 5)
        b1.add_book('The Hobbit', 4)
        b1.add_book('The Catcher in the Rye', 2)
        fav_books = b1.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
        self.assertTrue('The Hunger Games' in fav_books['book_name'].values)
        self.assertTrue('The Giver' in fav_books['book_name'].values)
        self.assertTrue('The Hobbit' in fav_books['book_name'].values)
        self.assertFalse('The Catcher in the Rye' in fav_books['book_name'].values)
                         
if __name__ == '__main__':
    
    unittest.main(verbosity=3)