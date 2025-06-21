import os

import pandas as pd

from src.Train.Train import Train


class Initialize:

    def run(self):
        input_dir = "input"
        os.makedirs(input_dir, exist_ok=True)
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        if not os.path.exists("input/data.csv"):
            raise FileNotFoundError("File 'input/data.csv' not found.")

        data = pd.read_csv("input/data.csv")
        train = Train(data)
        train.run()