import pandas as pd
import os

DATA_PATH = os.path.join("data", "dailyActivity_merged.csv")

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    with open("columns.txt", "w") as f:
        f.write("\n".join(df.columns.tolist()))
        f.write("\n\nFirst 2 rows:\n")
        f.write(str(df.head(2)))
    print("Columns written to columns.txt")
else:
    print("Data file not found.")
