from datetime import date
from datetime import time
class not_smoke:
    def __init__(self, start_date, price, timer):
        self.start_date = start_date
        self.price = price
        self.timer = timer

    def starting_date(self, result):
        self.result = self.start_date - date.now
        return result
    
    def money(self, saved_money):
        days = self.start_date - self.result
        self.saved_money = self.price * days
        return saved_money
    
    

    

