import unittest

class Account:
    def __init__(self, amount=None):
        self.amount = amount

    @property
    def am(self):
        return self.amount if self.amount else None

    @am.setter
    def am(self, value):
        self.amount = value

    @am.deleter
    def am(self):
        self.amount = None

me = Account(23)
# me.am = 11
del me.am

print(me.amount)