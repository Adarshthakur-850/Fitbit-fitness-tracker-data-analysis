import pandas as pd

def perform_eda(df):

    print("\n" + "="*40)
    print("Exploratory Data Analysis")
    print("="*40)

    print("\nDataset Info:")
    print(df.info())

    print("\nDescriptive Statistics:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nCorrelation with Calories:")
    if 'Calories' in df.columns:
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        print(numeric_df.corr()['Calories'].sort_values(ascending=False))
