import random


class CreditCard(dict):

    def is_valid(self):
        """Mock the check of card validity."""
        if len(self['cc_number']) == 16:
            return True
        return False

    def funds_available(self, amount):
        """Mock the check of funds in the account."""
        return random.choice([True, False])
