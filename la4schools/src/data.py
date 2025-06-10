import pandas as pd
import os.path

pd.set_option("display.max_columns", None)
path = os.path.dirname(__file__) + "\\LA4Schools (1).csv"
df = pd.read_csv(path)


