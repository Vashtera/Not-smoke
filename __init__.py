from datetime import datetime
from datetime import time
class not_smoke:
    def __init__(self, start_date, price):
        self.price = price
        start_date = datetime.strptime(start_date,"%d/%m/%y")
        with open("Not-smoke/start_date.txt", 'w') as start:
            start.write(start_date.strftime("%d/%m/%y"))
        self.start_date = start_date
    #This func just defines start date
    def starting_date(self):
        with open("Not-smoke/start_date.txt", 'r') as start:
            new_date = start.read()
        result = datetime.now() - datetime.strptime(new_date, "%d/%m/%y")
        self.result = result
    #This func just calc how much money I saved
    def money(self):
        self.saved_money = self.price * self.result.days
    #This func is restart date, and resets saved money
    def restart(self):
        self.start_date = datetime.now()
        with open("Not-smoke/start_date.txt", 'w') as start:
            start.write(datetime.now().strftime("%d/%m/%y"))
    #Info method
    def info(self):
        self.starting_date()
        self.money()
        print(f"Бросил курить: {self.start_date.strftime("%d/%m/%y")}, сэкономил: {self.saved_money}, не куришь уже: {self.result}")

start_date = input("Please enter your starting date(Day/Month/Year): ")
price_of_cigarettes = int(input("Please enter the price of cigarettes: "))
erbol = not_smoke(start_date, price_of_cigarettes)
choice = int(input("1 - Инфо, 2 - Сбросить: "))
if choice == 1:
    erbol.info()
elif choice == 2:
    erbol.restart()
    erbol.info()



    

