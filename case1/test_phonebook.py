import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def test_create_phonebook(self):
        phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        phonebook = Phonebook()
        phonebook.add("test1", "123456")
        self.assertEqual("123456", phonebook.lookup("test1"))

