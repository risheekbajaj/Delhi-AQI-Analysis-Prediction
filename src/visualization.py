# src/visualization.py
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set global style
sns.set_style("whitegrid")

def save_plot(fig, output_dir, filename):
    """
    Helper function to save figures to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    save_path = os.path.join(output_dir, filename)
    fig.savefig(save_path)
    print(f"Saved plot: {save_path}")
    plt.close(fig)

def plot_aqi_trend(df, output_dir):
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=df, x='Datetime', y='AQI', alpha=0.7, color='teal')
    plt.title('Daily AQI Trend in Delhi')
    plt.xlabel('Date')
    plt.ylabel('AQI')
    plt.tight_layout()
    save_plot(plt.gcf(), output_dir, 'aqi_trend.png')

def plot_monthly_avg(df, output_dir):
    monthly_aqi = df.groupby('Month')['AQI'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(data=monthly_aqi, x='Month', y='AQI', palette='Blues_d')
    plt.title('Average Monthly AQI')
    plt.tight_layout()
    save_plot(plt.gcf(), output_dir, 'monthly_aqi.png')

def plot_correlation(df, output_dir):
    plt.figure(figsize=(10, 8))
    corr = df[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone', 'AQI']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Pollutants')
    plt.tight_layout()
    save_plot(plt.gcf(), output_dir, 'correlation_heatmap.png')

def plot_seasonal_distribution(df, output_dir):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Season', y='AQI', order=['Winter', 'Summer', 'Monsoon', 'Post-Monsoon'], palette='Set2')
    plt.title('Seasonal AQI Distribution')
    plt.tight_layout()
    save_plot(plt.gcf(), output_dir, 'seasonal_aqi.png')

def plot_forecast_results(historical_df, forecast_df, output_dir):
    plt.figure(figsize=(12, 6))
    plt.plot(historical_df['Datetime'], historical_df['AQI'], label='Historical Data', alpha=0.5)
    plt.plot(forecast_df['Datetime'], forecast_df['Predicted_AQI'], label='Forecast (Next 12 Months)', color='orange', linewidth=2)
    plt.title('AQI Forecast: Historical vs Prediction')
    plt.legend()
    plt.tight_layout()
    save_plot(plt.gcf(), output_dir, 'aqi_forecast.png')