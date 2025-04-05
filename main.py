
from http.cookiejar import user_domain_match

from get_user import curr_account, new_account

hasAccount = input("Do you have an account? (Enter Y/N)").upper()
while hasAccount != "Y" or "N":
    hasAccount = input("Please enter Y or N").upper()
if hasAccount == "Y":
    userName = curr_account()
else:
    userName = new_account()



