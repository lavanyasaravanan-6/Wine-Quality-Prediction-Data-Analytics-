import pandas as pd

def load_data():

    red_wine = pd.read_csv("dataset/winequality-red.csv", sep=";")
    white_wine = pd.read_csv("dataset/winequality-white.csv", sep=";")

    red_wine["Wine_Type"] = "Red"
    white_wine["Wine_Type"] = "White"

    wine = pd.concat([red_wine, white_wine], ignore_index=True)

    print("Datasets loaded successfully!")

    return wine