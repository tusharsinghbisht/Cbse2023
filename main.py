# Logistic Management system.

import message
from animation import loading, animate
import orders
import auth
import os


if os.path.exists("./data") == False:
    os.mkdir("./data")

animate("\n\nHello, Welcome to THE LOGISTIC MANAGEMENT SYSTEM by tushar_coder!")

message.pink("\nEnter 1 to CREATE NEW ACCOUNT and 2 to LOGIN")

user = None

try:
    inp = int(input("-> "))

    if inp == 1:
        auth.register()
    elif inp == 2:
        user = auth.login()
    else:
        message.red("Invalid input")
        exit()

except ValueError:
    message.red("Sorry, Please enter either 1 or 2")
    exit()

if user == None:
    print("fa")
    exit()

loading()

animate("\nWelcome " + user["name"] +", feel free to use all the services\n\n")
message.blue("\nENTER FOLLOWING CODES TO GET YOUR WORK DONE -")
loading()

while True:
    print("___________________________________________________")
    print("\n1. ADD ORDER")
    print("2. UPDATE ORDER")
    print("3. DELETE ORDER")
    print("4. VIEW ALL ORDERS")
    print("5. VIEW IN PROGRESS ORDERS")
    print("6. VIEW SHIPPED ORDER")
    print("7. VIEW DELIVERED ORDER")
    print("8. VIEW CANCELLED ORDER")
    print("9. VIEW FAILED ORDER")
    print("10. SEARCH FOR ORDER")
    print("11. EXIT.")

    
    message.color("\nWhat you want to do next?", "blue", False)
    message.blue("ENTER CHOICE :")
    try:
        code = int(input("-> "))
    except ValueError:
        message.red("Invalid input X_X")
        continue

    if code == 1:
        orders.addOrder(user["userID"],)
        loading()

    elif code == 2:
        orders.updateOrderDetails(user["userID"])
        loading()

    elif code == 3:
        orders.deleteOrder(user["userID"])
        loading()

    
    elif code == 4:
        orders.viewAllOrders(user["userID"])
        loading()
    elif code == 5:
        orders.viewOrder(user["userID"],"ORDERED", "pink")
        loading()
    elif code == 6:
        orders.viewOrder(user["userID"],"SHIPPED", "cyan")
        loading()
    elif code == 7:
        orders.viewOrder(user["userID"],"DELIVERED", "green")
        loading()
    elif code == 8:
        orders.viewOrder(user["userID"],"CANCELLED", "yellow")
        loading()
    elif code == 9:
        orders.viewOrder(user["userID"],"FAILED", "red")
        loading()

    elif code == 10:
        orders.searchOrder(user["userID"])
        loading()

    elif code == 11:
        message.green("Exited successfully... ^_^ have a nice day " + user["name"] + " !")
        break

    else: 
        message.red("Please enter a valid code -_-")
        loading()



