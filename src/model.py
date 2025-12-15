# src/model.py
import pandas as pd
import numpy as np
import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_model(df):
    """
    Trains a Random Forest Regressor on the processed dataframe.
    """
    # 1. Feature Selection
    features = ['Month', 'Year', 'Days', 'Holidays_Count']
    target = 'AQI'
    
    # 2. Train-Test Split (Time-based split preferred for time series)
    # Using data before 2024 for training, and 2024 for testing
    split_date = '2024-01-01'
    train_mask = df['Datetime'] < split_date
    
    # Fallback to random split if date range is insufficient
    if train_mask.sum() == 0 or (~train_mask).sum() == 0:
        X = df[features]
        y = df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    else:
        X_train = df[train_mask][features]
        y_train = df[train_mask][target]
        X_test = df[~train_mask][features]
        y_test = df[~train_mask][target]
    
    # 3. Model Training
    print("Training Random Forest Model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluation
    y_pred = model.predict(X_test)
    metrics = {
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
        'MAE': mean_absolute_error(y_test, y_pred),
        'R2': r2_score(y_test, y_pred)
    }
    
    return model, metrics, X_test, y_test, y_pred

def generate_forecast(model, last_date, days=365):
    """
    Generates AQI predictions for the specified number of future days.
    """
    future_dates = [last_date + datetime.timedelta(days=x) for x in range(1, days + 1)]
    future_df = pd.DataFrame({'Datetime': future_dates})
    
    # Generate features for future dates
    future_df['Month'] = future_df['Datetime'].dt.month
    future_df['Year'] = future_df['Datetime'].dt.year
    future_df['Days'] = future_df['Datetime'].dt.dayofweek + 1
    # Assumption: Future holidays are not calculated here, set to 0 (or use a calendar library)
    future_df['Holidays_Count'] = 0 
    
    features = ['Month', 'Year', 'Days', 'Holidays_Count']
    future_df['Predicted_AQI'] = model.predict(future_df[features])
    
    return future_df