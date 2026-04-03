from datetime import date
from datetime import time
class not_smoke:
    def __init__(self, start_date, price):
        self.start_date = start_date
        self.price = price

    def starting_date(self, result):
        self.result = self.start_date - date.now
        return result
    
    def money(self, saved_money):
        days = self.start_date - self.result
        self.saved_money = self.price * days
        return saved_money
    
    def info(self):
        print(f"Бросил курить: {self.start_date}, сэкономил: {self.saved_money}, не куришь уже: {self.result}")

Erbol = not_smoke(2026-4-3, 1250)
Erbol.info()
    

    

