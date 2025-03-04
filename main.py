from data import MENU
from data import resources
from time import sleep

def coffee_report():
    """Prints the report of resources in coffee machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${format(resources['money'], '.2f')}")


def refill_machine():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Ingredients refilled. Yay, more coffee!")

def empty_coins():
    print(f"There was ${format(resources['money'], '.2f')} in the coffe machine.")
    resources["money"] = 0


def get_ingredients(drink):
    """Returns ingredients of the drink requested"""
    return MENU[drink]["ingredients"]


def get_price(drink):
    """Returns price of the drink requested"""
    return MENU[drink]["cost"]


def check_resources(drink):
    """Checks if there are enough resources in coffee machine to make drink.
    Returns True if enough resources, otherwise returns the depleted resource"""
    ingredients = get_ingredients(drink)
    if ingredients["water"] > resources["water"]:
        print(f"Sorry there is not enough water.")
        return False
    elif ingredients["coffee"] > resources["coffee"]:
        print(f"Sorry there is not enough coffee.")
        return False
    elif not drink == "espresso" and ingredients["milk"] > resources["milk"]:
        print(f"Sorry there is not enough milk.")
        return False
    else:
        return True


def process_coins(coins):
    """Returns the total of the coins inserted."""
    total = (.25 * coins["Quarters"]) + (.1 * coins["Dimes"]) + (.05 * coins["Nickels"]) + (.01 * coins["Pennies"])
    return total


def calculate_refund(price, total_received):
    """Returns the amount of refund"""
    return round(total_received - price, 2)


def make_coffee(drink, price):
    """Makes the coffee drink. Deducts ingredients from resources."""
    print(f"Brewing {drink}...")
    for ingredient in MENU[drink]["ingredients"]:
        amount = MENU[drink]["ingredients"][ingredient]
        resources[ingredient] -= amount

    sleep(2)
    print("Almost there...")
    sleep(2)
    resources["money"] += price
    print(f"Here is your {drink} ☕. Enjoy!")


def coffee_machine():
    stop_order = False
    while not stop_order:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input == "off":
            stop_order = True
        elif user_input == "report":
            coffee_report()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            enough_resources = check_resources(user_input)
            if enough_resources:
                price = get_price(user_input)
                print(f"Total cost of drink is ${format(price, '.2f')}")
                print("Please insert coins.")

                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                coins_inserted = {
                    "Quarters": quarters,
                    "Dimes": dimes,
                    "Nickels": nickels,
                    "Pennies": pennies
                }

                total_coins = process_coins(coins_inserted)
                if total_coins < price:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    refund = calculate_refund(price, total_coins)
                    print(f"Here is ${format(refund, '.2f')} in change.")
                    make_coffee(user_input, price)

        elif user_input == "refill":
            refill_machine()
        elif user_input == "cash out":
            empty_coins()
        else:
            print("Sorry that input is not recognized. Please try again")

# main
coffee_machine()