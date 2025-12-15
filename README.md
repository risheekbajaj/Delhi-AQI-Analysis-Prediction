# 🌫️ The Air Quality Story of Delhi: Analysis & Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Project Overview
**The Air Quality Story of Delhi** is an end-to-end data analytics and machine learning project that investigates the alarming air pollution trends in India's capital. 

Using historical data from 2021 to 2024, this project performs detailed **Exploratory Data Analysis (EDA)** to understand seasonal patterns and pollutant correlations. It further implements a **Random Forest Regressor** to predict future Air Quality Index (AQI) levels, providing actionable insights for policymakers and citizens.

## 🚀 Key Features
* **Data Cleaning & Preprocessing**: Handling missing values, datetime conversion, and seasonal feature engineering.
* **Comprehensive EDA**: Visualizing trends, monthly averages, and pollutant correlations using `matplotlib` and `seaborn`.
* **Predictive Modeling**: Forecasting AQI for the next 12 months using Random Forest (RMSE: ~68.70).
* **Automated Reporting**: Generating a professional PDF report with insights and plots using `reportlab`.

## 📂 Project Structure
```text
Delhi-AQI-Analysis-Prediction/
│
├── data/                          # Raw and processed datasets
│   └── final_dataset.csv
│
├── notebooks/                     # Jupyter Notebooks for experimentation
│   └── Delhi_AQI_Analysis.ipynb
│
├── src/                           # Source code modules
│   ├── __init__.py
│   ├── preprocessing.py           # Data cleaning & feature engineering
│   ├── visualization.py           # Plotting functions
│   ├── model.py                   # ML model training & forecasting
│   └── report.py                  # PDF report generation
│
├── outputs/                       # Generated artifacts
│   ├── figures/                   # Saved EDA & Forecast plots
│   └── reports/                   # Final PDF Report
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

```

##📊 Dataset DetailsThe dataset (`final_dataset.csv`) contains daily air quality records with the following key columns:

* **Date/Month/Year**: Temporal features.
* **Pollutants**: `PM2.5`, `PM10`, `NO2`, `SO2`, `CO`, `Ozone`.
* **Target**: `AQI` (Air Quality Index).
* **Derived**: `Season` (Winter, Summer, Monsoon, Post-Monsoon), `AQI_Category`.

##🛠️ Installation & Setup1. **Clone the Repository**
```bash
git clone [https://github.com/risheekbajaj/Delhi-AQI-Analysis-Prediction.git](https://github.com/risheekbajaj/Delhi-AQI-Analysis-Prediction.git)
cd Delhi-AQI-Analysis-Prediction

```


2. **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```



##💻 Usage###Option 1: Run the Jupyter NotebookOpen the notebook to see the step-by-step analysis and run the cells interactively.

```bash
jupyter notebook notebooks/Delhi_AQI_Analysis.ipynb

```

###Option 2: Run via Scripts (Modular)You can import the modules in your own scripts or run the notebook which calls these modules.

```python
from src.preprocessing import load_data, preprocess_data
from src.model import train_model

# Example workflow
df = load_data('data/final_dataset.csv')
clean_df = preprocess_data(df)
model, metrics, _, _, _ = train_model(clean_df)
print(metrics)

```

##🔍 Key Insights* **⚠️ Winter Crisis**: AQI consistently spikes to "Severe" levels (>400) during Winter (Nov-Jan) due to temperature inversion and low wind speeds.
* **☠️ Primary Pollutants**: **PM2.5** and **PM10** show a near-perfect correlation (r > 0.95) and are the biggest drivers of poor air quality.
* **🔮 Forecast**: The model predicts a recurrence of hazardous air quality in the upcoming winter season, suggesting the need for preemptive pollution control measures in October.

##📈 Visualizations| AQI Trend | Correlation Matrix |
| --- | --- |
|  |  |

##🤝 ContributingContributions are welcome! Please fork the repository and create a pull request for any feature enhancements or bug fixes.

##📜 LicenseThis project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---

*Created by Risheek Bajaj*

```

```