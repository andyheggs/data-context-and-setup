import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
         # 1) Build the absolute path to the csv folder
        csv_path = os.path.join(
            os.path.dirname(__file__),  # folder containing data.py
            '..',                       # go one folder up
            'data',                     # enter "data"
            'csv'                       # enter "csv"
        )

        # 2) Gather all CSV file names
        file_names = [f for f in os.listdir(csv_path) if f.endswith('.csv')]

        # 3) Build “key” names by removing "olist_" prefix and "_dataset" suffix if present
        key_names = []
        for name in file_names:
            key = name
            # Remove "_dataset.csv" if present, else remove just ".csv"
            if key.endswith('_dataset.csv'):
                key = key[:-len('_dataset.csv')]
            elif key.endswith('.csv'):
                key = key[:-len('.csv')]
            # Remove the prefix "olist_" if it exists
            if key.startswith('olist_'):
                key = key[len('olist_'):]
            key_names.append(key)

        # 4) Create a dict mapping each key to the corresponding DataFrame
        data = {}
        for fn, kn in zip(file_names, key_names):
            data[kn] = pd.read_csv(os.path.join(csv_path, fn))

        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
