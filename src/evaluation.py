from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np

def evaluate_models(models, scaler, X_test, y_test):

    print("\nEvaluating models...")
    results = []

    X_test_scaled = scaler.transform(X_test)

    for name, model in models.items():
        y_pred = model.predict(X_test_scaled)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)

        results.append({
            'Model': name,
            'MAE': mae,
            'RMSE': rmse,
            'R2 Score': r2
        })

        print(f"\n{name} Results:")
        print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.4f}")

    results_df = pd.DataFrame(results)
    print("\nModel Comparison:")
    print(results_df)
    return results_df
