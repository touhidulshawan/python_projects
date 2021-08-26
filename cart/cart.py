# create a dummy shopping cart

# global cart
cart = []


# function to add item
def add_item():
    try:
        items = [str(item) for item in input("Name of the Items: ").split(",")]
        if len(items) < 1:
            print("Can not be empty item")
            return add_item()
        else:
            for item in items:
                cart.append(item)
            print("Items added successfully to cart")
    except ValueError:
        print("Items should be separated by Comma(,)")
        return add_item()


# function to remove item
def remove_item():
    try:
        if len(cart) < 1:
            print("There is no item in the cart!")
            return
        else:
            item_to_remove = input("Enter the item name you want to remove: ")
            cart.remove(item_to_remove)
            print(f"{item_to_remove} is removed from cart.")
    except ValueError:
        print("Invalid input")
        return remove_item()


# function to update item on cart
def update_item():
    if len(cart) < 1:
        print("There is no item in the cart")
    else:
        item_to_update = input("Which item do you want to replace: ")
        if item_to_update in cart:
            new_item = input("Enter the new Item: ")
            item_index = cart.index(item_to_update)
            cart[item_index] = new_item
            print("Item replace sucessfully.")
        else:
            print("Not match with cart items")


# function to view the item/items
def display_cart():
    if len(cart) < 1:
        print("There is no item in cart!")
    else:
        print(f"There is {len(cart)} item/items in cart")
        for item in cart:
            print(f"- {item}")


exit_program = False

while not exit_program:
    print("""
    1. Add item to cart
    2. Remove item from cart
    3. View the cart
    4. Update Cart Item
    5. Exit the Program
    """)

    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        display_cart()
    elif choice == 4:
        update_item()
    elif choice == 5:
        exit_program = True
    else:
        print("Invalid choice input")
