import pandas as pd

def preprocess_data(df):

    print("Preprocessing data...")

    column_mapping = {
        'participant-id': 'Id',
        'timestamp': 'ActivityDate',
        'total-steps': 'TotalSteps',
        'total-distance': 'TotalDistance',
        'tracker-distance': 'TrackerDistance',
        'logged-activities-distance': 'LoggedActivitiesDistance',
        'very-active-distance': 'VeryActiveDistance',
        'moderately-active-distance': 'ModeratelyActiveDistance',
        'light-active-distance': 'LightActiveDistance',
        'sedentary-active-distance': 'SedentaryActiveDistance',
        'very-active-minutes': 'VeryActiveMinutes',
        'fairly-active-minutes': 'FairlyActiveMinutes',
        'lightly-active-minutes': 'LightlyActiveMinutes',
        'sedentary-minutes': 'SedentaryMinutes',
        'calories': 'Calories'
    }
    df.rename(columns=column_mapping, inplace=True)

    if 'ActivityDate' in df.columns:
        df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
        df['DayOfWeek'] = df['ActivityDate'].dt.day_name()
        df['Month'] = df['ActivityDate'].dt.month_name()

    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Removed {duplicates} duplicate rows.")
        df.drop_duplicates(inplace=True)

    if df.isnull().sum().sum() > 0:
        print("Handling missing values (filling with 0 for activity metrics)...")
        df.fillna(0, inplace=True)

    return df

if __name__ == "__main__":
    pass
