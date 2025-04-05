import os

def new_account():
        userName = input("Enter Username:")
        userName += ".csv"
        while os.path.exists(userName):
            userName = input("Username already exists. Please enter another: ")
        return userName

def curr_account():
    userName = input("Enter Username:")
    userName += ".csv"
    if not os.path.exists(userName):
        print("Username not found")
        while (not userName == "Yes") or (os.path.exists(userName)):
            userName = input("Enter a valid username or 'New' to create a new username")
            if userName.lower() == "new":
                userName = new_account()
                break
            userName += ".csv"
    return userName

