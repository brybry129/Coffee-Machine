from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep


def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    stop_order = False
    while not stop_order:
        user_input = input(f"What would you like?\n{menu.get_items()}").lower()
        if user_input == "off":
            stop_order = True
        elif user_input == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            drink = menu.find_drink(user_input)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

        elif user_input == "refill":
            coffee_maker.refill_machine()
        elif user_input == "cash out":
            money_machine.empty_coins()
        else:
            print("Sorry that input is not recognized. Please try again")


# main
coffee_machine()
