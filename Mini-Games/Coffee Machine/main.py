# My Coffee Machine
from menu import MENU, resources
from art import logo

print(logo)

coins = {"quarters": 0.25,
         "dimes" : 0.1,
         "nickles": 0.05,
         "pennies": 0.01
         }

def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")

switch = True
money = 0

while switch:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if customer_choice == "off":
        switch = False
        break
    elif customer_choice == "report":
        report()
    else:
        if MENU[customer_choice]['ingredients']['water'] > resources['water']:
            print("Sorry there is not enough water")
        elif MENU[customer_choice]['ingredients']['milk'] > resources['milk']:
            print("Sorry there is not enough milk")
        elif MENU[customer_choice]['ingredients']['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee")
        else:
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_input = quarters * coins['quarters'] + dimes * coins['dimes'] + nickles * coins['nickles'] + pennies * coins['pennies']
            drink_cost = MENU[customer_choice]['cost']
            if total_input > drink_cost:
                change = total_input - drink_cost
                resources['water'] -= MENU[customer_choice]['ingredients']['water']
                resources['milk'] -= MENU[customer_choice]['ingredients']['milk']
                resources['coffee'] -= MENU[customer_choice]['ingredients']['coffee']
                money += drink_cost
                print(f"Here is ${change} in change.")
                print(f"Here is your {customer_choice}, enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")

