from datetime import datetime
from datetime import time
class not_smoke:
    def __init__(self, start_date, price):
        start_date = datetime.strptime(start_date,"%d/%m/%y")
        self.start_date = start_date
        self.price = price
    #This func just defines start date
    def starting_date(self):
        result = datetime.now() - self.start_date
        self.result = result
    #This func just calc how much money I saved
    def money(self):
        self.saved_money = self.price * self.result.days
    #This func is restart date, and resets saved money
    def _restart(self):
        self.start_date = datetime.now()
        self.saved_money = 0
    #Info method
    def info(self):
        self.starting_date()
        self.money()
        print(f"Бросил курить: {self.start_date}, сэкономил: {self.saved_money}, не куришь уже: {self.result}")

erbol = not_smoke('3/4/26', 1250)
erbol.info()


    

