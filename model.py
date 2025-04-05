from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


def initialize_model(df) -> RandomForestClassifier:

    # Trains and tests the model
    # Returns a model with the most optimal parameters

    X = df.drop(columns=["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=11)

    random_forest = RandomForestClassifier(random_state=11)

    param_grid = {
        'n_estimators': [10, 50, 100, 200],  # Number of trees
        #'max_depth': [None, 10, 20, 30],  # Maximum depth of each tree
        'min_samples_split': [2, 5, 10],  # Minimum samples required to split an internal node
        'min_samples_leaf': [1, 2, 4],  # Minimum samples required to be at a leaf node
    }

    grid_search = GridSearchCV(estimator=random_forest, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)
    print(f"Best parameters found: {grid_search.best_params_}")
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    return RandomForestClassifier(**grid_search.best_params_, random_state=11)


def make_prediction(rf_model,predict_data):
    prediction = rf_model.predict(predict_data)
    return prediction

