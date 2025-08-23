'''Assignment: Build a Mini Inventory Tracker Using Lists
Objective: Create a Python program that manages a simple inventory system using lists. You'll simulate adding, removing, and updating items in stock.

Requirements:

Create a list called inventory with at least 5 items (strings).

Implement the following functions:

add_item(item) – adds an item to the inventory.
remove_item(item) – removes the item if it exists.
update_item(old_item, new_item) – replaces an existing item.
show_inventory() – prints the current inventory.
Add a menu system using a loop to let the user choose actions.
Bonus: Track item quantities using a list of tuples or nested lists.
'''

inventory = ["Sugar","Oil","Tomatoes","Milk","Eggs"]

def show_inventory():
    x=0 #numbers to show for items
    print("Available Items in Inventory:")
    for i in inventory: #i = iterator for items in inventory
        x+=1
        print(x,i)

def add_item(item):
    inventory.append(item)
    

def remove_item(item):
    inventory.remove(item)
    

def update_item(old_item, new_item):
    
    for old ,new in zip(old_item,new_item):
        if old in inventory:
            index = inventory.index(old)
            inventory[index]=new
            print(f"{old} replaced with {new}")
        else:
            print(f"{old } not found")
        


def menu():
    print('''
Available Menu Options:
Press 1 to Add Item in Inventory
Press 2 to Remove Item from Inventory
Press 3 to Update an Item in Inventory
Press 4 to Show the items in Inventory
Press 5 to Exit''')
    

while True:
    menu()
    print("x"*60)
    menu_input = int(input("Press Available option from  Menu."))

    if menu_input==1:
        user_input = input("Enter items to Add separated by commas: ")
        items = user_input.split(",")
        for i in items:
            add_item(i)
        print("Items:",user_input,"Added to inventory")
        show_inventory()
            
    elif menu_input==2:
        user_input = input("Enter items to Remove separated by commas: ")
        items = user_input.split(",")
        
        for i in items:
            if i not in inventory:
                print(f"Item:{i} not exist.enter correct item to remove")
            else:
                remove_item(i)
                print("Item:",i,"Removed from inventory")
        show_inventory()
              
        
    elif menu_input==3:
        
        show_inventory()
        
        old_item = input("Enter items Name to select separated by commas: ").split(",")
        new_item = input("Enter items to Replace separated by commas: ").split(",")
        update_item(old_item, new_item)
        show_inventory() 

    elif menu_input==4:
        show_inventory()
        
    elif menu_input==5:
        print("Thank you for Using Inventory System.")
        break
    else:
        print("Invalid Option Entered,please try again.")
        
        
        
        
        
  
        
        
    
    
   


