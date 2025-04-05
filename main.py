import os

from get_user import curr_account, new_account

hasAccount = input("Do you have an account? (Enter Y/N)").upper()
while hasAccount != "Y" or "N":
    hasAccount = input("Please enter Y or N").upper()
if hasAccount == "Y":
    userName = input("Enter Username:")
    userName += ".csv"
    if not os.path.exists(userName):
        userNameNew = curr_account()
else:
    userNameNew = new_account()



