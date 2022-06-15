from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

x=CoffeeMaker()
y=MoneyMachine()
z=Menu()


is_on=True
while is_on:
    choice=z.get_items()
    user=input("what do u want : {espresso/cappuccino/latte} ")
    if user=="off":
        is_on=False
    elif user=="report":
        x.report()
        y.report()
    else:
        drink=z.find_drink(user)
        if x.is_resource_sufficient(drink):
            if y.make_payment(drink.cost):
                x.make_coffee(drink)





