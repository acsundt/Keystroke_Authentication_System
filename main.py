import os
import time

from data_collector import collect, collect_predict, collect_training, combine_classifications, get_password, \
    training_to_df, transform_data
from get_user import curr_account, new_account
import pandas as pd

from model import initialize_model, make_prediction


def main():
    hasAccount = input("Do you have an account? (Enter Y/N) ").upper()
    while hasAccount != "Y" and hasAccount != "N":
        hasAccount = input("Please enter Y or N").upper()
    if hasAccount == "Y":
        userName = input("Enter Username:")
        userName += ".csv"
        if not os.path.exists(userName):
            userNameNew = curr_account()

        else:
            df = pd.read_csv(userName)
            rf_model = initialize_model(df)

            print("Enter Password: ")
            predict_transformed = collect_predict()
            prediction = make_prediction(rf_model,predict_transformed)
            print("Prediction: ", prediction)

    else:
        userNameNew = new_account()
        print("Choose a password. Press shift to submit it.")
        time.sleep(1)
        password = get_password(collect(1))
        time.sleep(2)
        print("Password: ", password)
        training_data_true = collect_training(1)

        training_data_false = collect_training(0)

        training_data_transformed_false = transform_data(training_data_false)
        training_data_transformed_true = transform_data(training_data_true)

        training_data = combine_classifications(training_data_transformed_false, training_data_transformed_true)

        df = training_to_df(training_data, password)
        df.to_csv(userNameNew, index=False)





main()