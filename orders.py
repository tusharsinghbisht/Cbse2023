import pickle
import message
from generate_random_id import getID
import datetime
from animation import loading

def addOrder(userID):
    try:
        f = open("./data/"+userID+"/orders.dat", "ab")

        message.pink("\nFill order details")

        message.blue("\nOrder Name: ")
        name = input("->")

        message.blue("\nOrdered by: ")
        orderby = input("->")

        message.blue("\nDelivery address: ")
        address = input("->")
        
        message.blue("\nOrder Cost: ")
        cost = int(input("->"))
        # Order Status: (1: ORDERED; 2: SHIPPED, 3: CANCELLED, 4: DELIVERED, 5: FAILED)

        if name == "" or orderby == "" or address == "":
            raise ValueError

        data = {
            "orderID": getID(),
            "orderBy": orderby,
            "address": address,
            "ORDERED_at": str(datetime.date.today()),
            "status": "ORDERED",
            "name": name,
            "cost": cost,
            "SHIPPED_at": "NA",
            "DELIVERED_at": "NA",
            "CANCELLED_at": "NA",
            "FAILED_at": "NA",
        }

        pickle.dump(data, f)
        f.close()

        loading()

        message.green("\nOrder successfully added :-).\n")
    except ValueError:
        message.red("Invalid input...X_X\n")


def getOrdersData(userID):

    try:
        f = open("./data/"+userID+"/orders.dat", "rb")
        data = []
        try:
            while True:
                data.append(pickle.load(f))

        except EOFError:
            pass

        f.close()

        if len(data) == 0:
            raise FileNotFoundError
        return data
    
    except FileNotFoundError:
        message.red("You don't have any data as of now first add it!")
        return []


def getOrderDetails(order, complete=False):
    print("-> ORDER ID =>", order["orderID"])
    print("-> ORDER NAME =>", order["name"])
    print("-> ORDERED BY =>", order["orderBy"])
    print("-> ADDRESS =>", order["address"])
    print("-> COST =>", order["cost"])
    print("-> STATUS =>", order["status"])
    print("-> ORDERED AT =>", order["ORDERED_at"])
    if complete:
        print("-> SHIPPED AT =>", order["SHIPPED_at"])
        print("-> DELIVERED AT =>", order["DELIVERED_at"])
        print("-> FAILED AT =>", order["FAILED_at"])

def viewAllOrders(userID):
    data = getOrdersData(userID)

    if len(data) == 0:
        return None
    
    loading()

    print("\n")
    print("_____________________________________________________________________________________________")

    print("{:<5} {:<25} {:<25} {:<10} {:<10} {:<20}".format('SNO.', 'ORDERID', 'NAME', 'COST', 'STATUS', 'DATE OF ORDER'))
    k=0
    for d in data:
        k+=1
        txt = "{:<5} {:<25} {:<25} {:<10} {:<10} {:<20}".format(k, d["orderID"], d["name"][0:25]+"..", d["cost"], d["status"], d["ORDERED_at"])

        if d["status"] == "ORDERED":
            print(txt)
        elif d["status"] == "SHIPPED":
            message.color(txt, "cyan", False)
        elif d["status"] == "CANCELLED":
            message.color(txt, "yellow", False)
        elif d["status"] == "DELIVERED":
            message.color(txt, "green", False)
        elif d["status"] == "FAILED":
            message.color(txt, "red", False)
    print("_____________________________________________________________________________________________")
    

    print("\n")
    message.pink("Total orders till now => "+str(len(data)))

def viewOrder(userID, status, color):
    data = getOrdersData(userID)

    if len(data) == 0:
        return None
    
    loading()

    print("\n")
    print("_____________________________________________________________________________________________")
    message.color("{:<5} {:<25} {:<25} {:<10} {:<10} {:<20}".format('SNo.', 'ORDERID', 'NAME', 'COST', 'STATUS', status+' AT'), color, False)
    k = 0
    for d in data:
        if d["status"] == status:
            k+=1
            print("{:<5} {:<25} {:<25} {:<10} {:<10} {:<20}".format(k, d["orderID"], d["name"][0:25]+"..", d["cost"], d["status"], d[status+"_at"]))
    print("_____________________________________________________________________________________________")


    print("\n")
    message.color("Total orders "+ status +" => "+str(k), color)


def deleteOrder(userID):
    message.blue("Enter order ID to delete order: ")
    ID = input("->")

    data = getOrdersData(userID)
    data_new = []
    found = False
    for i in data:
        if i["orderID"] == ID:
            found=True
        else:
            data_new.append(i)
    
    loading()
    if found: 
        f = open("./data/" + userID+"/orders.dat", "wb")
        for i in data_new:
            pickle.dump(i, f)
        message.green("Deleted order with ID - " + ID)
    
    else:
        message.red("Can't find the order with id provided ;-;")

    
def updateOrderDetails(userID):
    message.blue("\nEnter order ID to update: ")
    ID = input("->")

    data = getOrdersData(userID)
    data_new = []
    order = None
    found = False
    updated=True
    for i in data:
        if i["orderID"] == ID:
            found=True

            message.pink("\nOrder details -\n")
            
            getOrderDetails(i)

            message.yellow("\nWhat do you want to update ? enter code to select")

            while True:
                print("\n1 = Edit name")
                print("2 = Edit cost")
                print("3 = Edit ordered by")
                print("4 = Edit address")
                print("5 = Edit order status")
                print("6 = No updates")

                try:
                    c = int(input("\nEnter code - "))
                except ValueError:
                    message.red("Invalid input X_X")
                
                if c == 1:
                    message.blue("\nEnter New Name: ")
                    i["name"] = input("-> ")
                    break
                
                elif c == 2:
                    message.blue("\nEnter New Cost: ")
                    i["cost"] = input("-> ")
                    break

                elif c == 3:
                    message.blue("\nEnter new Reciever: ")
                    i["orderBy"] = input("-> ")
                    break

                elif c == 4:
                    message.blue("\nEnter new address: ")
                    i["address"] = input("-> ")
                    break

                elif c == 5:
                    while True:
                        message.yellow("\nUse follwing codes to set order status")
                        print("\n1 => ORDERED")
                        print("2 => SHIPPED")
                        print("3 => DELIVERED")
                        print("4 => CANCELLED")
                        print("5 => FAILED\n")

                        message.color("CURRENT STATUS: "+i["status"], "cyan", False)
                        try:
                            x = int(input("\nEnter: "))
                        except ValueError:
                            message.red("Invalid input X_X")

                        if x == 1:
                            i["status"] = "ORDERED"
                            break
                        elif x == 2:
                            i["status"] = "SHIPPED"
                            i["SHIPPED_at"] = str(datetime.date.today())
                            break
                        elif x == 3:
                            i["status"] = "DELIVERED"
                            i["DELIVERED_at"] = str(datetime.date.today())
                            break
                        elif x == 4:
                            i["status"] = "CANCELLED"
                            i["CANCELLED_at"] = str(datetime.date.today())
                            break
                        elif x == 5:
                            i["status"] = "FAILED"
                            i["FAILED_at"] = str(datetime.date.today())
                            break
                        else:
                            message.red("\nEnter a valid status code (1 to 5)")

                    break
                elif c == 6:
                    message.green("\nSure, if you want no updates!")
                    updated = False
                    break

                else: 
                    message.red("\nEnter valid code (1 to 6)!")

            order = i
            
            data_new.append(i)
        else:
            data_new.append(i)
    
    loading()

    if found and updated and order != None: 
        f = open("./data/"+userID+"/orders.dat", "wb")
        for i in data_new:
            pickle.dump(i, f)
        message.green("Updated order with ID - " + ID)
        message.pink("\nOrder details -\n")
            
        getOrderDetails(order)

    elif found:
        message.green("No updates are done to order with ID - " + ID)

    else:
        message.red("Can't find any order with id provided ;-;")


def searchOrder(userID): 
    message.yellow("\nEnter order ID to search: ")
    ID = input("->")
    

    data = getOrdersData(userID)
    order = None
    found = False
    for i in data:
        if i["orderID"] == ID:
            found=True
            order = i
    
    loading()
    if found and order != None: 
        message.green("\nSuccessfully Found order the with ID - " + ID)
        message.green("Order Complete Details are - ")
        getOrderDetails(order,True)

    
    else:
        message.red("Can't find any order with id provided ;-;")
