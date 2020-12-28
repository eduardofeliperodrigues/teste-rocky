import pandas as pd
import numpy as np

def read_data():
    return pd.read_json("broken-database.txt")

def correct_names(data):
    replace_dict = {"æ":"a", "¢":"c","ø":"o","ß":"b"}
    data["name"].replace(to_replace=replace_dict, regex=True, inplace=True)

def correct_price(data):
    data["price"].astype(np.float64)

def correct_quantity(data):
    data["quantity"] = data["quantity"].fillna(0)

def export_json(data):
    data.to_json("saida.json", orient="records")

def main():
    data = read_data()
    correct_names(data)
    correct_price(data)
    correct_quantity(data)
    export_json(data)


if __name__ == '__main__':
    main()