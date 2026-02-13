from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os

MODELS_DIR = "models"

def prepare_modeling_data(df):

    features = ['TotalSteps', 'TotalDistance', 'VeryActiveMinutes', 
                'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes',
                'ActivityIntensityScore', 'IsWeekend']

    target = 'Calories'

    df_model = df.dropna(subset=features + [target])

    X = df_model[features]
    y = df_model[target]

    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_models(X_train, y_train):

    print("Training models...")

    if not os.path.exists(MODELS_DIR):
         os.makedirs(MODELS_DIR)

    models = {
        'LinearRegression': LinearRegression(),
        'RandomForestRegressor': RandomForestRegressor(n_estimators=100, random_state=42)
    }

    trained_models = {}

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    joblib.dump(scaler, os.path.join(MODELS_DIR, 'scaler.pkl'))

    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train_scaled, y_train)
        trained_models[name] = model

        joblib.dump(model, os.path.join(MODELS_DIR, f'{name}.pkl'))

        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='r2')
        print(f"{name} CV R2 Score: {cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

    return trained_models, scaler
