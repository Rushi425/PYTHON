menu = {
    "vadapav": 10,
    "pani puri": 20,
    "bhel puri": 30,
    "dosa": 40,
    "idli": 50,
    "vadasambhar": 60
}


print("Welcome to Hotel Rushi's Era")
print("-------------------------------")

total_bill = 0    

while True:
    print("\n1. Order Food")
    print("2. View Menu")
    print("3. Pay Bill")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        item_1 = input("Enter a item name you want: ").lower()

        if item_1 in menu:
            total_bill += menu[item_1]
            print(f"Your order of {item_1} is received successfully.")
        else:
            print("Sorry, we don't have this item in our menu.")

    elif choice == "2":
        print("\nOur Menu is as follows:")
        for key, value in menu.items():
            print(f"{key}: {value} Rs")

    elif choice == "3":
        print(f"Your total bill is {total_bill} Rs")

    elif choice == "4":
        if total_bill > 0:
            print(f"Your total bill is {total_bill} Rs")
            print("Thank you for visiting Hotel Rushi's Era. Have a great day!")
        else:
            print("Thank you for visiting Hotel Rushi's Era. Have a great day!")
        break