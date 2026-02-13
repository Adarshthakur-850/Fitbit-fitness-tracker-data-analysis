import pandas as pd
import numpy as np

def create_features(df):

    print("Feature Engineering...")

    df['TotalActiveMinutes'] = df['VeryActiveMinutes'] + df['FairlyActiveMinutes'] + df['LightlyActiveMinutes']

    df['ActivityIntensityScore'] = (
        (df['VeryActiveMinutes'] * 3) + 
        (df['FairlyActiveMinutes'] * 2) + 
        (df['LightlyActiveMinutes'] * 1)
    )

    df['CaloriesPerStep'] = df['Calories'] / (df['TotalSteps'] + 1)

    if 'DayOfWeek' in df.columns:
        df['IsWeekend'] = df['DayOfWeek'].isin(['Saturday', 'Sunday']).astype(int)

    return df
