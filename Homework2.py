# Name: Jacob Schenkelberg
# Section: D
# Project: Vending Machine
# Description:

# Creating initial variables
state = "A"
total_inserted = 0
drink_1 = 2 # Coke $1.50
drink_2 = 4 # Pepsi $1.50
drink_3 = 1 # Sprite $1.50
machine = True
total_cost = 0
change = 0
drink_list = ["Items selected: "]

# Defining State machines

while state != "G":
    if(state == "F"):
        print("\nRestocking")
    if(state == "A"):
        input_start = input("\nEnter (start) to start the program: ")
        if input_start == "start" or input_start == "Start":
            state = "B"
        else:
            print("\nYou need to type start in order to start. ")
    if(state == "B"):
        input_coins = input("\nInsert money or press (y) for refund: ")
        if(input_coins == "Y" or input_coins == "y"):
            state = "E"
        else:
            input_coins = float(input_coins)
            total_coins = input_coins # temporary variable
            if(input_coins > 1.50):
                state = "C"
            else:
                print("Enter in more money.")
    if(state == "C"):
        temp_drink_cost = 1.50
        print("\n(1) What drink do you want? Options: (Coke,Pepsi,Sprite)\n(2) Are you finished with your drink selection? (y)\n(3) Would you like a refund? (r)\n")
        print("Coke ($1.50) \nPepsi ($1.50) \nSprite ($1.50)")
        drink_input = input("\nEnter: ")
        if(drink_input == "Y" or drink_input == "y"):
            state = "D"
        if(drink_input == "R" or drink_input == "r"):
            state = "E"
        if(drink_1 > 0):
            if(drink_input == "Coke" or drink_input == "coke"):
                drink_1 = drink_1 - 1
                input_coins = input_coins - 1.50
                print("\nCoke added to list.")
                drink_list.append("Coke $1.50 ")
                total_cost += 1.50
        else:
            print("\nNo Coke available. Please select another option.\n")
        if(drink_2 > 0):
            if(drink_input == "Pepsi" or drink_input == "pepsi"):
                drink_2 = drink_2 - 1
                input_coins = input_coins - 1.50
                print("\nPepsi added to list.")
                drink_list.append("Pepsi $1.50 ")
                total_cost += 1.50
        else:
            print("\nNo Pepsi available. Please select another option.\n")
        if(drink_3 > 0):           
            if(drink_input == "Sprite" or drink_input == "sprite"):
                drink_3 = drink_3 - 1
                input_coins = input_coins - 1.50
                print("\nSprite added to list.")
                drink_list.append("Sprite $1.50")
                total_cost += 1.50
        else:
            print("\nNo Sprite available. Please select another option.\n")
    if(state == "D"):
        drink_list.append("TOTAL COST: {}".format(total_cost))
        print(drink_list)
        drink_list = ["Items selected: "] # resets the list
        change = total_coins - total_cost
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
        
        