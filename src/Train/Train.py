import pandas as pd
from sentence_transformers import SentenceTransformer

class Train:

    data = None

    def __init__(self, data: pd.DataFrame):
        self.data = data

    def run(self):
        data = self.data

        model = SentenceTransformer('all-MiniLM-L6-v2')
