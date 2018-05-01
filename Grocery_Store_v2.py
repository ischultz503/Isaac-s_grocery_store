#!/usr/bin/env python
import copy
import random

# Isaac Schultz
# April 26, 2018
# Sitka Tech Junior Software Engineer 

class Grocery_product(object):
    def __init__(self, name, unit, price, quantity):
        self.name = name
        self.unit = unit
        self.price = price
        self.quantity = quantity

    def get_name(self):
        name = self.name

    def get_price(self):
        price = self.price

    def get_quantity(self):
        quantity = self.quantity

    def get_unit(self):
        unit = self.unit


class Grocery_options(object):
    def __init__(self):
        self.contents = {}
    
    def item_exists(self, name):
        return name in self.contents

    def add_item(self, item):
        self.contents[item.name] = item
        
    def remove_item(self, item):
        del self.contents[item.name]

    def get_item(self, name):
        return self.contents[name]

    def get_contents(self):
        all_items = []

        for key in self.contents:
            item = self.contents[key]
            all_items.append(item)

        return all_items

    def get_contents_by_price(self):
        all_items = []
        pricemap = {}

        for key in self.contents:
            item = self.contents[key]
            subtotal = item.quantity * item.price
            pricemap[subtotal] = item

        for key in pricemap:
            item = pricemap[key]
            all_items.append(item)

        return all_items
    
    def get_total(self):
        total = 0

        for key in self.contents:
            item = self.contents[key]
            subtotal = item.quantity * item.price
            total = total + subtotal

        return total

    def getItemCount(self):
        return self.contents.size

def welcome_message():
    print("\n\nHELLO! Welcome to Isaac's local grocery store, we are so happy you came! We might not have the widest selection, but we make sure that everything we do have is the very best around!\n\nIs there something you're looking for that you don't see on the shelves? No problem, Isaac can order anything you want and have it on our shelves in seconds! Just select option 6 below to place an order.")

def display_prompt():
    print("\nPlease continue by selecting one of the options below. \n\n 1. View all available items \n 2. View cart \n 3. Add item to cart \n 4. Remove item from cart \n 5. Clear cart \n 6. Order new item, anything in the world! \n 7. Check out and exit\n\nPlease select an option by entering a number 1 through 6\n\n")

def display_grocery_list(groceries, show_subtotals = False):
    for item in groceries:
        if show_subtotals:
            subtotal = item.quantity * item.price
            print("Item: ", item.name, " Quantity: ", item.quantity, " ", item.unit, " Subtotal: $", format(subtotal, ".2f"), sep = '')
        else:
            print("Item: ", item.name, " Price: $", format(item.price, ".2f"), " / ", item.unit, sep = '')
            
    

if __name__ == "__main__":
    #Set up inital store selection with default items
    crab = Grocery_product("Crab", "lb.", 45., 0)
    kombucha = Grocery_product("Kombucha", "oz.", .25, 0)
    apple = Grocery_product("Apple", "lb.", 1.5, 0)
    prosciutto = Grocery_product("Prosciutto", "oz.", 2., 0)
    cheese_cake = Grocery_product("Cheesecake", "slice", 3.25, 0)
    kale = Grocery_product("Kale", "bunch", 3.50, 0)
    heirloom_tomatoes = Grocery_product("Heirloom Tomatoes", "lb.", 5.99, 0)
    coffee = Grocery_product("Coffee", "lb.", 12.99, 0)
    caviar = Grocery_product("Caviar", "oz.", 75., 0)
    ravioli = Grocery_product("Ravioli", "lb.", 5.50, 0)
    salmon = Grocery_product("Salmon", "lb.", 14.99, 0)
    rice = Grocery_product("Rice", "lb.", 1.99, 0)
    couscous = Grocery_product("Couscous", "lb.", 2.40, 0) 

    #Build 2 dicts, one for the shopping cart and one for the store selection
    cart = Grocery_options()
    all_groceries = Grocery_options()
    
    #Populate the store list with some default options
    all_groceries.add_item(crab)
    all_groceries.add_item(kombucha)
    all_groceries.add_item(apple)
    all_groceries.add_item(prosciutto)
    all_groceries.add_item(cheese_cake)
    all_groceries.add_item(kale)
    all_groceries.add_item(heirloom_tomatoes)
    all_groceries.add_item(coffee)
    all_groceries.add_item(caviar)
    all_groceries.add_item(ravioli)
    all_groceries.add_item(salmon)
    all_groceries.add_item(rice)
    all_groceries.add_item(couscous)
    
    #This is where the user input comes in, the program will run until done_shopping is True
    done_shopping = False
    welcome_message()

    while not done_shopping:
        display_prompt() 
        choice = input()
        if choice == "1":
            #Display all avaiable items in the store
            all_contents = all_groceries.get_contents()
            print("Here is what we have on the shelves today:\n")
            display_grocery_list(all_contents)
        
        elif choice == "2":
            #Display current contents of cart
            print("Enter 1 to sort items in cart by name. Enter 2 to sort by subtotal")
            choice2 = input()
            print("These are the items in your cart at the moment:\n")
            if choice2 == "1":
                all_contents = cart.get_contents()
            else:
                all_contents = cart.get_contents_by_price()

            display_grocery_list(all_contents, True)

        elif choice == "3":
            #Add an item to your cart
            print("Here's what we have on the shelves at the moment:\n")
            display_grocery_list(all_groceries.get_contents())
            print("\nWhich item would you like to add to your cart? Please enter the item name as it appears above\n")
            item_name = input()
            item = copy.copy(all_groceries.get_item(item_name))

            if item:
                #Check to see if item is available, then add desired amount
                print("How much ", item.name, " do you want to add to your cart? It's going for $", format(float(item.price), ".2f"), " per ", item.unit, " today (Enter quantity)\n", sep = '')
                valid = False
                while not valid:
                    item.quantity = input()
                    try:
                        item.quantity = int(item.quantity)
                        valid = True
                    except ValueError:
                        print("Please enter a whole number")

                cart.add_item(item)
                print("Woohoo! You added", item.name, "to your cart\n")

            else:
                #Item doesn't currently exist in list of available items.
                print("Sorry, item:", item_name, "is not available at the moment. Don't hesitate to ask if you want Isaac to order it for you.\n")
        
        elif choice == "4":
            #Remove an item from your cart
            display_grocery_list(cart.get_contents())
            print("\nWhich item do you want to remove from your cart?")
            item_name = input()
            if cart.item_exists(item_name):
                #Check to see if item is in cart, then remove.
                item = cart.get_item(item_name)
                cart.remove_item(item)
                print(item.name, "has been removed from your cart.\n")
            else:
                print("\nSorry but acording to me records you don't have that item in your cart\n")

        elif choice == "5":
            #Clear all items from cart
            print("\nAre you sure you want to clear your shopping cart? Type 'yes' to confirm\n")
            choice2 = input()
            if choice2 == "yes" or choice2 == "y":
                #Reset cart back to default cart settings
                cart = Grocery_options()

        elif choice == "6":
            #Add new product to the available items, user inputs name and a suggested price, store price will be close input.
            print("Isaac would be happy to order you anything you'd like! \n\nWhat item do you want to order?\n")
            name = input()
            print("\nIt's been years since Isaac stocked ", name, ", would you be kind enough to remind him what unit ", name, " is typically sold by? (eg. lb. or oz.) \n", sep = '')
            unit = input()
            print("\nWe will see what we can find for you! What do you consider to be a reasonable price per ", unit, " for ", name, "?\n", sep ='')
            suggestion_price = float(input())
            store_price = float(suggestion_price) * round(random.uniform(.56, 1.23),2)
            item = Grocery_product(name, unit, store_price, 0)
            all_groceries.add_item(item)
            if store_price >= suggestion_price:
                # Message if the price found was above what was requested
                print("\nOK, ", item.name, " has been added to the store! Looks like ", item.name, " is out of season. $", format(store_price, ".2f"), " per ", item.unit," was the best price Isaac could find.\n", sep = '')
            else:
                print("\nOK, ", item.name, " has been added to the store! We found a great deal for you at just $", format(store_price, ".2f"), " per ", item.unit, "\n", sep = '')
        
        elif choice == "7":
            #Check out
            #all_contents = all_groceries.get_contents()
            print("\nAre you sure you are all done shopping?\n")
            answer = input()
            if answer == "yes" or answer == "y":
                cost = cart.get_total()
                print("\nWe hope you found everything you were looking for, how would you like to pay today? 1. Cash 2. Credit 3. Bitcoin\n")
                choice2 = input()
                if choice2 == "1":
                    #Cash payment option
                    print("\nYour total is $", format(cost, ".2f"),". How much cash will you be paying with?\n", sep = '')
                    cash = float(input())
                    if cash < float(cost):
                        print("\nSorry but that's not enough to cover your total, please enter an amount greater than $", format(cost, ".2f") ,"\n", sep ='')
                    else:
                        change = cash - cost
                        print("\nThank you for shopping with us today, your change is $", format(change, ".2f"), " have a nice day and we hope to see again you very soon!\n", sep = '')
                        done_shopping = True 
                
                elif choice2 == "2":
                    #Credit card payment option
                    print("\nYour total is $", format(cost, ".2f"), ", but seeing as this isn't a real store we can't really take credit cards. So just enter whatever you want!\n")
                    response = input()
                    print("\nGreat answer, I'll pass it along to Isaac for you. Thanks again for shopping with us and we hope to see again soon!\n")
                    done_shopping = True

                elif choice2 == "3":
                    #Bitcoin payment option
                    #btc_price=XXXX
                    #btc_total=btc_price/cost
                    print("\nThe current BTC price is: $", format(cost, ".2f"), ". Please enter a bitcoin address below and send  BTC to me\n")
                    done_shopping = True 
