"""
Name: Jessica Yang
Date: Nov 5 2019
Program: Assignment 1, Good Morning America
Program Description: Computes the cost of breakfast at the Good Morning America restaurant
"""

# Cost of all the foods
EGG_COST = 0.99
BACON_COST = 0.49
SAUSAGE_COST = 1.49
HASH_BROWN_COST = 1.19
TOAST_COST = 0.79
COFFEE_COST = 1.09
TEA_COST = 0.89
SMALL_BREAKFAST = EGG_COST + HASH_BROWN_COST + TOAST_COST*2 + BACON_COST*2 + SAUSAGE_COST
REGULAR_BREAKFAST = EGG_COST*2 + HASH_BROWN_COST + TOAST_COST*2 + BACON_COST*4 + SAUSAGE_COST*2
BIG_BREAKFAST = EGG_COST*3 + HASH_BROWN_COST*2 + TOAST_COST*4 + BACON_COST*6 + SAUSAGE_COST*3


# Cost and Tax Variable
totalCost = 0.0
tax = 0


# Formats the breakfast input order to accept upper lower case and spaces
def format_input(text_line):
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line


# loop continues to prompt user for order input until q is entered
while True:
    order = input("Enter item (q to terminate) : small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
    # calls for the format input method to format the order
    order = format_input(order)
    # repeats question in a loop until the user inputs a valid order if the first order an invalid order
    while order != "egg" and order != "bacon" and order != "sausage" and order != "hash brown" and order != "toast" and order != "coffee" and order != "tea" and order != "small breakfast" and order != "regular breakfast" and order != "large breakfast":
        print("Error. Invalid order")
        order = input("Enter item (q to terminate) : small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
        # calls for the format input method to format the order
        order = format_input(order)
    # if q is entered, stops the while loop to calculate totals
    if order == "q":
        break
    # prompts user for amount of food requested
    amount = input("Enter quantity: ")
    # if the amount of food is not a number, then keeps prompting user for number and then turns the order into a number
    while not amount.isnumeric():
        print("Not valid number")
        amount = input("Enter quantity: ")
    if amount.isnumeric():
        amount = int(amount)
    # depending on which order was entered, adds its cost to the total cost
    if order == "egg":
        totalCost += EGG_COST*amount
    elif order == "bacon":
        totalCost += BACON_COST*amount
    elif order == "sausage":
        totalCost += SAUSAGE_COST*amount
    elif order == "hash brown":
        totalCost += HASH_BROWN_COST*amount
    elif order == "toast":
        totalCost += TOAST_COST*amount
    elif order == "coffee":
        totalCost += COFFEE_COST*amount
    elif order == "tea":
        totalCost += TEA_COST*amount
    elif order == "small breakfast":
        totalCost += SMALL_BREAKFAST*amount
    elif order == "regular breakfast":
        totalCost += REGULAR_BREAKFAST*amount
    elif order == "big breakfast":
        totalCost += BIG_BREAKFAST*amount


# rounds total cost and calculates tax
totalCost = round(totalCost, 2)
tax = round(totalCost*0.13, 2)

# prints the total cost, tax and overall total with tax
print("Cost: ", totalCost, "\nTax: ", tax, "\nTotal: ", totalCost+tax)




