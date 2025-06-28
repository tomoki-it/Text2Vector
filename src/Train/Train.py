import json

import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

class Train:

    data = None

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def run(self) -> list:
        data = self.data
        data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

        model = SentenceTransformer('all-MiniLM-L6-v2')
        data["embedding"] = data["headline"].apply(lambda x: model.encode(x))

        with open("differential.json") as f:
            price_diff = json.load(f)

        diff_df = pd.DataFrame(price_diff).T
        diff_df.index.name = "date"
        diff_df = diff_df.rename(columns={"Diff": "btc_diff"}).reset_index()

        merged_df = pd.merge(data, diff_df, on="date")

        x = np.stack(merged_df["embedding"].values)
        y = merged_df["btc_diff"].values

        #test
        return [x, y]

