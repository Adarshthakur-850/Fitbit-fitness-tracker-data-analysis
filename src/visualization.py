import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

PLOTS_DIR = "plots"

def save_plot(fig, filename):
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)
    filepath = os.path.join(PLOTS_DIR, filename)
    fig.savefig(filepath)
    print(f"Plot saved to {filepath}")
    plt.close(fig)

def plot_activity_vs_calories(df):

    print("Plotting Activity vs Calories...")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='TotalSteps', y='Calories', data=df, hue='VeryActiveMinutes', size='VeryActiveMinutes', sizes=(20, 200), ax=ax)
    ax.set_title('Total Steps vs Calories Burned')
    save_plot(fig, 'steps_vs_calories.png')

def plot_daily_activity_dist(df):

    print("Plotting Activity Distributions...")
    fig, ax = plt.subplots(figsize=(12, 6))
    cols = ['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes']
    sns.boxplot(data=df[cols], ax=ax)
    ax.set_title('Distribution of Activity Minutes')
    save_plot(fig, 'activity_minutes_dist.png')

def plot_correlations(df):

    print("Plotting Correlation Heatmap...")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Correlation Heatmap')
    save_plot(fig, 'correlation_heatmap.png')

def plot_day_of_week_activity(df):

    print("Plotting Day of Week Activity...")
    if 'DayOfWeek' in df.columns:
        order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='DayOfWeek', y='TotalSteps', data=df, order=order, ax=ax)
        ax.set_title('Average Total Steps by Day of Week')
        save_plot(fig, 'day_of_week_activity.png')
