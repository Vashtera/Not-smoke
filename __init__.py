from datetime import datetime
from datetime import time
class not_smoke:
    def __init__(self, start_date, price):
        start_date = datetime.strptime(start_date,"%d/%m/%y")
        self.start_date = start_date
        self.price = price

    def calculate_all(self):
        self.result = datetime.now() - self.start_date 
        self.saved_money = self.result.days * self.price 
    
    def info(self):
        self.calculate_all()
        print(f"Бросил курить: {self.start_date}, сэкономил: {self.saved_money}, не куришь уже: {self.result}")

erbol = not_smoke('3/4/26', 1250)
print(erbol.info())


    

