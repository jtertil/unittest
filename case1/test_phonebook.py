import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    # setUp method -> runner will run that method prior to each test
    def setUp(self):
        self.phonebook = Phonebook()

    # tearDown method -> runner will run that method after each test

    def test_lookup_entry_by_name(self):
        self.phonebook.add("test1", "12345")
        self.assertEqual("12345", self.phonebook.lookup("test1"))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_book_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("test1", "12345")
        self.phonebook.add("test2", "67890")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("test1", "12345")
        self.phonebook.add("test2", "12345")
        self.assertFalse(self.phonebook.is_consistent())


    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("test1", "12345")
        self.phonebook.add("test2", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("test1", "12345")
        self.assertIn("test1", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())