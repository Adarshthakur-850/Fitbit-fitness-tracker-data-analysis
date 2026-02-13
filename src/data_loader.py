import pandas as pd
import os
import requests

DATA_URL = "https://raw.githubusercontent.com/health-hacks/datasets/master/fitbit-mturk/various-participants/fitabase-data-3-12-16-to-4-11-16/dailyActivity_merged.csv"
DATA_PATH = os.path.join("data", "dailyActivity_merged.csv")

def load_data():

    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_PATH):
        print(f"Downloading data from {DATA_URL}...")
        try:
            response = requests.get(DATA_URL)
            response.raise_for_status()
            with open(DATA_PATH, 'wb') as f:
                f.write(response.content)
            print("Download complete.")
        except Exception as e:
            print(f"Error downloading data: {e}")
            raise

    print(f"Loading data from {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    print(f"Data loaded. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    load_data()
