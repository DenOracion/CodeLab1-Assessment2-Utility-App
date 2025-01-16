# Vending Machine Program
# Establishing items inside the vending machine
# Some parts of the code has been created and the code was revised with the assistance of the AI engine ChatGPT 
items = {
    'A1' : {'name': "Lay's Classic Chips", 'price': 2, 'stock': 6 },
    'A2' : {'name': "Lay's Salt & Vinegar Chips", 'price': 2.10, 'stock': 11 },
    'A3' : {'name': "Doritos Nacho Cheese", 'price': 1.70, 'stock': 14 },
    'A4' : {'name': "Cheetos Cheddar Jalapeno", 'price': 3, 'stock': 4 },
    'B1' : {'name': "Dr. Pepper", 'price': 1.50, 'stock': 13 },
    'B2' : {'name': "Coca-Cola", 'price': 1.25, 'stock': 8 },
    'B3' : {'name': "Sprite", 'price': 1.25, 'stock': 10 },
    'B4' : {'name': "Dasani Water", 'price': 1.15, 'stock': 6 },
    'C1' : {'name': "David's Sunflower Seeds", 'price': 2, 'stock': 15 },
    'C2' : {'name': "Lifesavers Mint", 'price': 1, 'stock': 5 },
    'C3' : {'name': "Jack Link's Original Beef Jerky", 'price': 7, 'stock': 9 },
    'C4' : {'name': "Nature Valley Oats & Honey Granola Bar", 'price': 2, 'stock': 15 },
} 
def display_items(): #The coding of this function was assisted with AI engines
    """This function shows the items inside the vending machine, their price, and their stock"""
    # This will calculate how long each column will be
    max_code_length = max(len(code) for code in items.keys())
    max_name_length = max(len(item['name']) for item in items.values())
    max_price_length = max(len(f"{item['price']:.2f}")for item in items.values())
    max_stock_length = max(len(str(item['stock'])) for item in items.values())

    # This allows the header to be printed with dynamic widths
    header = (
        f"{'Code':<{max_code_length}} "
        f"{'Item':<{max_name_length}} "
        f"{'Price':<{max_price_length}} "
        f"{'Stock':<{max_stock_length}} "
    )
    print("\n--- Vending Machine Items ---")
    print(header)
    print("-" * len(header)) # Underlines the header designed with dashed lines

    # Code to print each item
    for code, item in items.items():
        print(
            f"{code:<{max_code_length}}  "
            f"{item['name']:<{max_name_length}}  "
            f"${item['price']:<{max_price_length}.2f}  "
            f"{item['stock']:<{max_stock_length}}  "
        )
# Calls the function to display the items of the vending machine
display_items()

def asking_user_to_order():
    """Asks the user to select an item they want using its code number"""
    return input("Please enter the code of the item you wish to select: ").upper()

def handling_transaction(price):
    """Manages user's payment, guaranteeing the user pays the correct amount and returns potential change"""
    print(f"The item's costs ${price:.2f}.") # shows how much the user will have to pay for the item they want
    inserted_amount = 0.0
    while inserted_amount < price:
        try:
            amount = float(input(f"Please insert ${price - inserted_amount:.2f}. Insert amount: "))
            if amount <= 0:
                print("Please insert the correct amount.") 
                continue
            inserted_amount += amount
        except ValueError: # activates if a user inputs an unaccepted input (ex: xyz)
            print("Please insert a valid numerical amount.") 

    change = inserted_amount - price
    print(f"Transaction completed. The change returned is ${change:.2f}.")
    return change # lines 41-43 calculate the change needed and returns it to the user.

def give_item(code):
    """Dispenses the item of the selected code if available"""
    item = items[code]
    if item['stock'] > 0: # Checks if the vending machine still has the item in stock
        item['stock'] -= 1 # If it is still in stock deducts 1 from the current stock 
        print(f"Dispensing {item['name']}.") # Dispenses the item
    else:
        print(f"Sorry, {item['name']} is unavailable.") # If there is no more stock, print out that the item is unavailable

def run_vending():
    """Primary function to make the vending machine run"""
    while True:
        code = asking_user_to_order() # asks the user to input the code of the item they want

        if code not in items:
            print("Please enter a valid code.") # if the code inputted is not on the menu, asks the user to input a valid one
            continue

        item = items[code]
        if item['stock'] <= 0:
            print(f"Sorry this item is out of stock.") # informs the user that the item is out of stock
            continue

        handling_transaction(item['price'])
        give_item(code) # Gives out the item 

        # Asks the customer if they want anything else
        order_again = input("\n Do you wish to purchase another item? (yes/no):").strip().lower()
        if order_again != "yes":
            print("Thank you for your purchase!")
            break

# Function to execute the program
if __name__ == "__main__":
    run_vending()