import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add("test1", "123456")
        self.assertEqual("123456", phonebook.lookup("test1"))

    def test_missing_entry_raises_KeyError(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing")

    @unittest.skip("temp")
    def test_empty_book_is_consistent(self):
        phonebook = Phonebook()
        self.assertTrue(phonebook.is_consistent())
