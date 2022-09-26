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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 5. Input no. of quarters, dimes nickles and pennies:
quarters = float(input("how many quarters?:"))
dimes = float(input("how many dimes?:"))
nickles = float(input("how many nickles?:"))
pennies = float(input("how many pennies?:"))
# TODO: 6. Converted quarters, dimes nickles and pennies into dollars
quarter = quarters * 0.25
print(quarter)
dime = dimes * 0.1
print(dime)
nickle = nickles * 0.05
print(nickle)
penny = pennies * 0.01
print(penny)
# TODO: 7 Caltulate total money entered:
total_money_entered = penny + dime + nickle + quarter
print(f"Total amount entered is $ {total_money_entered}")

#TODO: 2. Check the user’s input:
if prompt == "espresso":
    print("Espresso")
elif prompt == "latte":
    print("Latte")
elif prompt == "cappuccino":
    print("Cappuccino")
elif prompt == "off":
    print("MACHINE IS OFF")

#TODO: 3. Amount used and remaining:
#For espresso:
#WATER:
water_needed = MENU["espresso"]["ingredients"]["water"]
water_left = 300 - int(water_needed)
print(f"Amount of water needed for espresso is {water_needed} ml. ")
print(f"Water amount remaining is {water_left} ml. ")
#COFFEE:
coffee_needed = MENU["espresso"]["ingredients"]["coffee"]
coffee_left = 100 - int(coffee_needed)
print(f"Amount of coffee needed for espresso is {coffee_needed} g. ")
print(f"Coffee amount remaining is {coffee_left} g. ")
#MILK:
milk_needed = MENU["espresso"]["ingredients"]["milk"]
milk_left = 200 - int(milk_needed)
print(f"Amount of milk needed for espresso is {milk_needed} ml. ")
print(f"Milk amount remaining is {milk_left} ml. ")
#COST:
cost_needed = MENU["espresso"]["cost"]
change = amount_entered - cost_needed
print(f"Here is your remaining {change} $")
#For latte:
#For cappucino:

#TODO: 4. Report:
print(f"Water left: {water_left}ml \n Milk left: {milk_left}ml \n Coffee left: {coffee_left}g \n and money left is :  ")


















































