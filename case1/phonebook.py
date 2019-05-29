class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def get_names(self):
        return self.entries.keys()

    def get_numbers(self):
        return self.entries.values()

    def is_consistent(self):

        # chceck for duplicate entries
        if len(self.entries) != len(set(self.entries.values())):
            return False

        # chceck for numbers that prefix one another
        for number in self.entries.values():
            for value in self.entries.values():
                if value == number:
                    pass
                elif value.startswith(number):
                    return False
        else:
            return True