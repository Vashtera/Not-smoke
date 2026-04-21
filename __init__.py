from datetime import datetime
from datetime import time
class not_smoke:
    def __init__(self, start_date, price):
        start_date = datetime.strptime(start_date,"%d/%m/%y")
        self.start_date = start_date
        self.price = price
        with open("start_date.txt", 'w') as start:
            start.write(str(start_date))
    #This func just defines start date
    def starting_date(self):
        with open("start_date.txt", 'r') as start:
            new_date = start.read()
        result = datetime.strptime(new_date) - self.start_date
        self.result = result
    #This func just calc how much money I saved
    def money(self):
        self.saved_money = self.price * self.result.days
    #This func is restart date, and resets saved money
    def restart(self):
        with open("start_date.txt", 'w') as start:
            start.write(str(datetime.now()))
    #Info method
    def info(self):
        self.starting_date()
        self.money()
        print(f"Бросил курить: {self.start_date}, сэкономил: {self.saved_money}, не куришь уже: {self.result}")

start_date = input("Please enter your starting date(Day/Month/Year): ")
price_of_cigarettes = int(input("Please enter the price of cigarettes: "))
erbol = not_smoke(start_date, price_of_cigarettes)
choice = int(input("1 - Инфо, 2 - Сбросить: "))
if choice == 1:
    erbol.info()
elif choice == 2:
    erbol.restart()
    erbol.info()



    

