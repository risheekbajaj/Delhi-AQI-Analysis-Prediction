# src/preprocessing.py
import pandas as pd
import os

def load_data(filepath):
    """
    Loads the dataset from the specified filepath.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} was not found.")
    return pd.read_csv(filepath)

def get_season(month):
    """
    Maps a month number (1-12) to a season in Delhi.
    """
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5, 6]:
        return 'Summer'
    elif month in [7, 8, 9]:
        return 'Monsoon'
    else:
        return 'Post-Monsoon'

def get_aqi_category(aqi):
    """
    Maps AQI values to their respective standard categories.
    """
    if aqi <= 50: return 'Good'
    elif aqi <= 100: return 'Satisfactory'
    elif aqi <= 200: return 'Moderate'
    elif aqi <= 300: return 'Poor'
    elif aqi <= 400: return 'Very Poor'
    else: return 'Severe'

def preprocess_data(df):
    """
    Main function to clean data and create new features.
    """
    df = df.copy()
    
    # 1. Create Datetime Column
    # Aggregating Year, Month, Date columns into a single datetime object
    df['Datetime'] = pd.to_datetime(df[['Year', 'Month', 'Date']].astype(str).agg('-'.join, axis=1))
    
    # 2. Season Engineering
    df['Season'] = df['Month'].apply(get_season)
    
    # 3. AQI Categorization
    df['AQI_Category'] = df['AQI'].apply(get_aqi_category)
    
    # 4. Sorting
    df = df.sort_values('Datetime').reset_index(drop=True)
    
    return df