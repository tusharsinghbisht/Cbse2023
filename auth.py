import message
import os
from animation import loading
import pickle
from string import punctuation
from pwinput import pwinput as getpass

def login():
    message.blue("\nEnter USERID: ")
    userID = input("-> ")

    dr = "./data/" + userID
    if os.path.exists(dr):
        f = open(dr + "/info.dat", "rb")
        data = pickle.load(f)
        f.close()
        if data["userID"] == userID:
            message.blue("Enter PASSWORD: ")
            pw = getpass("-> ")
            if pw == data["password"]:
                loading()
                message.green("Logged in Successfully!")
                return ["SUCCESS", data]
            else:
                loading()
                message.red("Oops.. looks like its a wrong password")
                message.cyan("No worries you can try again..")
                return ["FAILURE"]
    else:
        loading()
        message.red("User with this User ID do not exist")
        message.cyan("Try out login with a differnt ID")
        return ["FAILURE"]


def register():
    while True:
        name = ""
        userID = ""
        password = ""

        message.blue("\nEnter NAME :- ")
        name = input("-> ")

        if name.strip() == "":
            message.red("Invalid name")
            message.blue("Register Again!\n\n")
            continue

        message.blue("Enter USERID:- ")
        message.color("No special characters are allowed!", "yellow", False)
        userID = input("-> ")

        if userID.strip() == "" or any(p in userID for p in punctuation):
            message.red("Invalid User ID")
            message.blue("Register Again!\n\n")
            continue

        if os.path.exists("./data/" + userID):
            message.red("User with similar ID exists")
            message.blue("Try to login please or use a different User ID")
            return ["FAILURE"]

        message.blue("Enter PASSWORD (Must have 8 char atleast) :- ")
        while True:
            password = getpass("-> ")

            if password.strip() == "":
                message.red("Password can't be empty")
                message.blue("Enter password Again!")
                continue

            if len(password) < 8:
                message.red("Password must have 8 character atleast")
                message.blue("Enter password Again!")
                continue
            
            message.yellow("Please confirm your password -")
            confirm_pw = getpass("->")

            if confirm_pw != password:
                message.red("Passwords don't match")
                message.blue("Enter password Again!")
                continue


            message.cyan("Password confirmed!\n")
            break

        break

    loading()
    dr = "./data/" + userID
    os.mkdir(dr)
    f = open(dr + "/info.dat", "ab")
    data = { "name": name, "userID": userID, "password": password}
    pickle.dump(data,f)
    f.close()
    message.green("Successfully created a new user account!")
    return ["SUCCESS", data]