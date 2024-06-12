menu={
    'Pizza':50,
    'Pasta':40,
    'Chhhola Samosa':30,
    'Manchurian':40,
    'Glass-coke':40,
    'Chawmine-full':50,
    'Burger':60,
    'Cheese Burger':80,
    'Coffee':40,
    'Tea':20
}
#greet to the customer
print("Welcome to the Mishra resturant")
print("Pizza: Rs50\nPasta:40\nChhhola Samosa:30\nManchurian:40\nGlass-coke:40\nChawmine-full:50\nBurger:60\nCheese Burger:80\nCoffee:40\nTea:20")

order_total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print("Order item {item_1} is not available")
    
another_order=input("Do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2=input("Enter the name of second item =")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")