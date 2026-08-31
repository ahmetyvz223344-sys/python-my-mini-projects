

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu_class=Menu()

latte=MenuItem("latte",200,150,24,2.5)
espresso=MenuItem("espresso",50,0,16,1.5)
cappucino=MenuItem("cappucino",250,100,24,3)


while True:
    option = menu_class.get_items()
    order_name = input(f"What would you like? {option}")


    if order_name=="report":
        money_machine.report()
        coffee_maker.report()
    else:




        drink=menu_class.find_drink(order_name)



        if coffee_maker.is_resource_sufficient(drink)==True and money_machine.make_payment(drink.cost)==True:
            coffee_maker.make_coffee(drink)



