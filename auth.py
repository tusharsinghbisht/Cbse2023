import message
import os
from animation import loading
import pickle
from string import punctuation

def login():
    message.blue("Enter USERID: ")
    userID = input("-> ")

    dr = "./data/" + userID

    if os.path.exists(dr):
        f = open(dr + "/info.dat", "rb")
        data = pickle.load(f)
        f.close()
        if data["userID"] == userID:
            message.blue("Enter PASSWORD: ")
            pw = input("-> ")
            if pw == data["password"]:
                loading()
                message.green("Logged in Successfully!")
                return data
            else:
                message.red("Oops.. looks like its a wrong password")
                exit()
    else:
        message.red("User with this User ID do not exist")
        exit()


def register():
    name = ""
    userID = ""
    password = ""

    while True:
        message.blue("\nEnter Name :- ")
        name = input("-> ")

        if name.strip() == "":
            message.red("Invalid name")
            message.blue("Register Again!\n\n")
            exit()

        message.blue("Enter User ID:- ")
        message.color("No special characters are allowed!", "yellow", False)
        userID = input("-> ")

        if userID.strip() == "" or any(p in userID for p in punctuation):
            message.red("Invalid UserID")
            message.blue("Register Again!\n\n")
            exit()

        if os.path.exists("./data/" + userID):
            message.red("User with similar ID exists")
            message.blue("Try to login please or use a different User ID")
            exit()

        message.blue("Enter Password (Must have 8 char atleast) :- ")
        password = input("-> ")
        if password.strip() == "":
            message.red("Invalid Password")
            message.blue("Register Again!\n\n")
            exit()

        if len(password) < 8:
            message.red("Password must have 8 char atleast")
            message.blue("Register Again!\n\n")
            exit()

        break

    loading()
    dr = "./data/" + userID
    os.mkdir(dr)
    f = open(dr + "/info.dat", "ab")
    data = { "name": name, "userID": userID, "password": password}
    pickle.dump(data,f)
    f.close()
    message.green("Successfully created a new user account! you can login now")
    exit()