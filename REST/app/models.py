import random


class CreditCard(object):
    
    def __init__(self, cc_number, owner_first_name=None, owner_last_name=None, expiration_date=None, ccv=None):
        self.cc_number = cc_number
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.expiration_date = expiration_date
        self.ccv = ccv

    def is_valid(self):
        """Mock the check of card validity."""
        if len(self.cc_number) == 16:
            return True
        return False

    def funds_available(self, amount):
        """Mock the check of funds in the account."""
        return random.choice([True, False])
