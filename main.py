MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """loop through each ingredient and check if there's enough"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item] #lets say water needed is 200 we check if resources is less or more.
        # Then we do the same for milk and then for coffee
            print(f"Sorry there is not {item}")
            return False
    return True #if we have looped through all items and there is enough resource

def process_coins():
    """Returns the total $ calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total #returns the total value
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}100ml")
        print(f"Milk: {resources['milk']}50ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink) #{'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}, 'cost': 2.5}
        if is_resources_sufficient(drink["ingredients"]):#takes 'ingredients': {'water': 200, 'milk': 150, 'coffee': 24}





















































