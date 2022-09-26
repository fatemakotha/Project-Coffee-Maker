MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()


#TODO: 2. Check the user’s input
if prompt == "espresso":
    print("Espresso")
elif prompt == "latte":
    print("Latte")
elif prompt == "cappuccino":
    print("Cappuccino")
elif prompt == "off":
    print("MACHINE IS OFF")

#For espresso:

water_needed = MENU["espresso"]["ingredients"]["water"]
water_left = 300 - int(water_needed)
print(f"Amount of water needed for espresso is {water_needed} ml. ")
print(f"Water amount remaining is {water_left} ml. ")


















































