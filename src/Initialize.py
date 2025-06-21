import os

class Initialize:

    def run(self):
        input_dir = "input"
        os.makedirs(input_dir, exist_ok=True)
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        if not os.path.exists("input/data"):
            raise FileNotFoundError("File 'input/data' not found.")
