from datetime import datetime
from datetime import time
class not_smoke:
    def __init__(self, start_date, price):
        self.start_date = start_date
        start_date = datetime.strptime(start_date,"%d/%m/%y")
        self.price = price

    def starting_date(self, result):
        self.result = result
        result = self.start_date - datetime.now()
        return result
    
    def money(self, saved_money):
        self.saved_money = saved_money
        saved_money = self.price * self.result
        return
    
    def info(self):
        print(f"Бросил курить: {self.start_date}, сэкономил: {self.saved_money}, не куришь уже: {self.result}")

erbol = not_smoke('3/4/26', 1250)
erbol.info()


    

