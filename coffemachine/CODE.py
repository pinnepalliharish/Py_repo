import random
from main import MENU,resources,profit

def is_resources_sufficient(order_ingredients):
    for k in order_ingredients:
        if order_ingredients[k]>=resources[k]:
            print(f"Sorry there is not enough {k}.")
            return False
    return True
def coins():
    print("please insert some coins : ")
    quaters=int(input("how many quaters : "))*0.25
    dimes=int(input("how many dimes : "))*0.1
    nickles=int(input("how many nickels : "))*0.05
    pennies=int(input("how many pennies : "))*0.01
    total=quaters+dimes+nickles+pennies
    return total
def is_cash_sufficient(cash_given,actual_cost):
    if cash_given>=actual_cost:
        change=round(cash_given-actual_cost,2)
        print(f"change is ${change}.")
        global profit
        profit+=actual_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def final(drink,order_ingredients):
    for k in order_ingredients:
        resources[k]-=order_ingredients[k]
    print(f"here is ur {drink}")
condition= True
while condition:
    user=input( "What would you like? (espresso/latte/cappuccino):")
    if user=="off":
        condition=False
    elif user=="report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money:${profit}")
    else:
        drink=MENU[user]
        if is_resources_sufficient(drink['ingredients']):
            cash=coins()
            if is_cash_sufficient(cash,drink['cost']):
                final(user,drink['ingredients'])





