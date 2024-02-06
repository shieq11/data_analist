from data import MENU, resources


def machine():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    set_off = True

    while set_off:
        choose = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choose == "off":
            set_off = False
        elif choose == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        elif choose in MENU.keys():

            if water < MENU[choose]["ingredients"]["water"]:
                print("Sorry there is not enough water")

            elif coffee < MENU[choose]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee")

            elif milk < MENU[choose]["ingredients"]["milk"]:
                print("Sorry there is not enough milk")

            else:
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                user_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.005 + pennies * 0.01

                if user_money > MENU[choose]["cost"]:
                    money += MENU[choose]["cost"]
                    change = user_money - MENU[choose]["cost"]
                    water -= MENU[choose]["ingredients"]["water"]
                    milk -= MENU[choose]["ingredients"]["milk"]
                    coffee -= MENU[choose]["ingredients"]["coffee"]
                    print(f"Here is ${change} in change\nHere is your {choose}. Enjoy")
                else:
                    print("Sorry that's not enough money. Money refunded")

        else:
            print("You type wrong product")


machine()
