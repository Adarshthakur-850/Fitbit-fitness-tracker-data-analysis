import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'src'))

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.eda import perform_eda
from src.visualization import plot_activity_vs_calories, plot_daily_activity_dist, plot_correlations, plot_day_of_week_activity
from src.feature_engineering import create_features
from src.model_trainer import prepare_modeling_data, train_models
from src.evaluation import evaluate_models

def main():
    print("Starting Fitbit Data Analysis Pipeline...")

    df = load_data()

    df = preprocess_data(df)

    perform_eda(df)

    df = create_features(df)

    plot_activity_vs_calories(df)
    plot_daily_activity_dist(df)
    plot_correlations(df)
    plot_day_of_week_activity(df)

    X_train, X_test, y_train, y_test = prepare_modeling_data(df)
    trained_models, scaler = train_models(X_train, y_train)

    evaluate_models(trained_models, scaler, X_test, y_test)

    print("\nPipeline completed successfully!")

if __name__ == "__main__":
    main()
