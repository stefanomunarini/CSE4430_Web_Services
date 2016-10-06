import random


class CreditCard(object):
    cc_number = None
    owner_first_name = None
    owner_last_name = None
    expiration_date = None
    ccv = None
    
    def __init__(self, cc_number, owner_first_name, owner_last_name, expiration_date, ccv):
        self.cc_number = cc_number
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.expiration_date = expiration_date
        self.ccv = ccv

    def is_valid(self):
        if len(self.cc_number) == 16:
            return True
        return False

    def funds_available(self, amount):
        return random.choice([True, False])
