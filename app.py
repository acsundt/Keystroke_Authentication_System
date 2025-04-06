from flask import Flask, render_template, request, redirect, url_for
import os
import json
import pandas as pd

from model import initialize_model, make_prediction
from data_collector import collect, collect_training, combine_classifications, get_password, training_to_df, transform_data

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
  username = request.form["username"]
  password = request.form["password"]
  timings_json = request.form["timings"]

  user_file = f"{username}.csv"
  if not os.path.exists(user_file):
    return redirect(url_for("register", error="User not found. Please register."))

  try:
    durations = json.loads(timings_json)
    df = pd.read_csv(user_file)
    model = initialize_model(df)

    if len(password) != len(durations):
      return "Password and timing length mismatch."

    input_df = pd.DataFrame([durations], columns=list(password))
    prediction = make_prediction(model, input_df)

    if prediction[0] == 1:
      return f"Welcome back, {username}!"
    else:
      return "Typing pattern did not match. Access denied."

  except Exception as e:
    return f"Error: {e}"

@app.route("/register")
def register():
  return render_template("register.html", error=request.args.get("error"))

@app.route("/create_account", methods=["POST"])
def create_account():
  username = request.form["username"]
  if os.path.exists(f"{username}.csv"):
    return redirect(url_for("register", error="Username already exists."))

  try:
    # Ask user to type password and collect it
    password = get_password(collect(1))

    # Collect training data for real and fake attempts
    training_data_true = collect_training(1)
    training_data_false = collect_training(0)

    # Transform and combine
    transformed_true = transform_data(training_data_true)
    transformed_false = transform_data(training_data_false)
    training_data = combine_classifications(transformed_false, transformed_true)

    df = training_to_df(training_data, password)
    df.to_csv(f"{username}.csv", index=False)

    return f"Account created for {username}. Password saved: {password}"

  except Exception as e:
    return f"Error during account creation: {e}"

if __name__ == "__main__":
  app.run(debug=True)
