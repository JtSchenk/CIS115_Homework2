# Name: Jacob Schenkelberg
# Section: D
# Project: Vending Machine
# Description:

# Creating initial variables
state = "A"
total_inserted = 0
MAX_SIZE_COKE = 2
MAX_SIZE_PEPSI = 4
MAX_SIZE_SPRITE = 1
drink_1 = MAX_SIZE_COKE  # Coke $1.50
drink_2 = MAX_SIZE_PEPSI # Pepsi $1.50
drink_3 = MAX_SIZE_SPRITE # Sprite $1.50
machine = True
total_cost = 0
change = 0
drink_list = ["Items selected: "]
drink_cost = 1.50

# Defining State machines

while state != "G":

    if(state == "A"):
        if(drink_1 < MAX_SIZE_COKE or drink_2 < MAX_SIZE_PEPSI or drink_3 < MAX_SIZE_SPRITE):
            state = "F"
        if(state == "A"):
            input_start = input("\nEnter (start) to start the program: ")
            if input_start == "start" or input_start == "Start":
                state = "B"
            else:
                print("\nYou need to type start in order to start. ")

    if(state == "B"):
        input_coins = input("\nInsert money or press (y) for refund: ")
        if(input_coins == "Y" or input_coins == "y"):
            change = 0
            state = "E"
        else:
            input_coins = float(input_coins)
            total_coins = input_coins # another coin variable to avoid conflicts
            if(input_coins >= 1.50):
                state = "C"
            else:
                print("Enter in more money.")

    if(state == "C"):
        print("\n(1) What drink do you want? Options: (Coke,Pepsi,Sprite)\n(2) Are you finished with your drink selection? (y)\n(3) Would you like a refund? (r)\n")
        print("Coke ($1.50) \nPepsi ($1.50) \nSprite ($1.50)")
        drink_input = input("\nEnter: ")
        if(drink_input == "Y" or drink_input == "y"):
            state = "D"
        if(drink_input == "R" or drink_input == "r"):
            change = input_coins
            drink_list = ["Items selected: "]
            state = "E"
        if(drink_input == "Coke" or drink_input == "coke"):
            if(drink_cost <= total_coins):
                if(drink_1 > 0):
                    drink_1 = drink_1 - 1
                    total_coins = total_coins - 1.50
                    print("\nCoke added to list.")
                    drink_list.append("Coke $1.50 ")
                    total_cost += 1.50
                else:
                    print("\nNo Coke available. Please select another option.\n")
            else:
                print("\nNot enough money for Coke.")
        if(drink_input == "Pepsi" or drink_input == "pepsi"):
            if(drink_cost <= total_coins):
                if(drink_2 > 0):
                    drink_2 = drink_2 - 1
                    total_coins = total_coins - 1.50
                    print("\nPepsi added to list.")
                    drink_list.append("Pepsi $1.50 ")
                    total_cost += 1.50
                else:
                    print("\nNo Pepsi available. Please select another option.\n")
            else:
                print("\nNot enough money for Pepsi.")
        if(drink_input == "Sprite" or drink_input == "sprite"):
            if(drink_cost <= total_coins):           
                if(drink_3 > 0):
                    drink_3 = drink_3 - 1
                    total_coins = total_coins - 1.50
                    print("\nSprite added to list.")
                    drink_list.append("Sprite $1.50")
                    total_cost += 1.50
                else:
                    print("\nNo Sprite available. Please select another option.\n")
            else:
                print("\nNot enough money for Sprite.")

    if(state == "D"):
        drink_list.append("TOTAL COST: {}".format(total_cost))
        print(drink_list)
        drink_list = ["Items selected: "] # resets the list
        change = input_coins - total_cost # original input coins - total cost
        if(change == 0):
            print("\nNo change required. All coins spent.")
            state = "A"
            total_cost = 0 # resets the total_cost
        else:
            state = "E"

    if(state == "E"):
        print("\nReturning change: ${}".format(change))
        change = 0 # resets the change
        total_cost = 0 # resets the total_cost
        state = "A"

    if(state == "F"):
        print("\nRestocking")
        drink_1 = MAX_SIZE_COKE
        drink_2 = MAX_SIZE_PEPSI
        drink_3 = MAX_SIZE_SPRITE
        state = "A"