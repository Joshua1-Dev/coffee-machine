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

water = 300
milk = 200
coffee = 100
money = 0

again = True

while again == True:
    choice = input("what would you like to drink? (espresso, latte or cappacino): ")
    if choice == "report":
        print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
    elif choice == "off":
        print('machine turned off')

    elif choice == "espresso":
        print("insert your coins")
        quater = int(input("how many quaters?: "))
        dime = int(input("how many dime?: "))
        nickle = int(input("how many nickle?: "))
        penny = int(input("how many penny?: "))

        quaters = quater * 0.25
        dimes = dime * 0.1
        nickles = nickle * 0.05
        pennies = penny *0.01

        total_amount = quaters + dimes + nickles + pennies
        if total_amount >= 2.5:
            if water > 50 and coffee > 24:
                water -= 50
                coffee -= 18
                money += 1.5
                change = total_amount - 1.5
                print(f"here is your espresso\nhere is your change {change}")
                print(f"resource after purchase = water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
            else:
                again = False
                print("there is shortage of resources")
    elif choice == "latte":
        print("insert your coins")
        quater = int(input("how many quaters?: "))
        dime = int(input("how many dime?: "))
        nickle = int(input("how many nickle?: "))
        penny = int(input("how many penny?: "))

        quaters = quater * 0.25
        dimes = dime * 0.1
        nickles = nickle * 0.05
        pennies = penny *0.01

        total_amount = quaters + dimes + nickles + pennies
        if total_amount >= 2.5:
            if water > 200 and milk > 150:
                water -= 200
                coffee -= 24
                money += 2.5
                milk -= 150
                change = total_amount - 2.5
                print(f"here is your latte\nhere is your change {change}")
                print(f"resource after purchase = water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
            else:
                again = False
                print("there is shortage of resources")
        else:
            print(f"{total_amount} is not up to $2.5")
            print(f"here is your refund {total_amount}")


    elif choice == "capachino":
        print("insert your coins")
        quater = int(input("how many quaters?: "))
        dime = int(input("how many dime?: "))
        nickle = int(input("how many nickle?: "))
        penny = int(input("how many penny?: "))

        quaters = quater * 0.25
        dimes = dime * 0.1
        nickles = nickle * 0.05
        pennies = penny *0.01

        total_amount = quaters + dimes + nickles + pennies
        if total_amount >= 3:
            if water > 200 or milk > 100:
                water -= 250
                coffee -= 24
                money += 3
                milk -= 100
                change = total_amount - 3
                print(f"here is your capachino\nhere is your change ${change}")
                print(f"resource after purchase = water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}")
            else:
                again = False
                print("there is shortage of resources")
        else:
            print(f"{total_amount} is not up to $1.5")
            print(f"here is your refund {total_amount}")

