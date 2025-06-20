from time import sleep


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, drink):
        """Makes the coffee drink. Deducts ingredients from resources."""
        print(f"Brewing {drink.name.capitalize()}...")
        for ingredient in drink.ingredients:
            self.resources[ingredient] -= drink.ingredients[ingredient]

        sleep(2)
        print("Almost there...")
        sleep(2)
        print(f"Here is your {drink.name.capitalize()} ☕. Enjoy!")

    def refill_machine(self):
        self.resources["water"] = 300
        self.resources["milk"] = 200
        self.resources["coffee"] = 100
        print("Ingredients refilled. Yay, more coffee!")
