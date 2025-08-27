# Health Insurance Premium Predictor

A **Streamlit-based web application** that predicts **health insurance premiums in INR** using a trained **statistical regression machine learning model**.  

---

## Features
- User-friendly Streamlit interface.
- Collects demographic, lifestyle, and health-related inputs.
- Predicts insurance premiums in **Indian National Rupees (INR)**.
- Built with **OOP principles** for scalability and maintainability.
- Pre-trained ML model stored using `joblib`.

## Project Pipeline  

1. **Data Preprocessing & Cleaning**  
   - Handled missing values and inconsistent entries.  
   - **Univariate analysis** for numeric features.  
   - Outlier treatment using statistical thresholds.  
   - Categorical analysis with count plots and frequency checks.  

2. **Exploratory Data Analysis (EDA)**  
   - Bivariate analysis for numeric–numeric and numeric–categorical relationships.  
   - Categorical–categorical analysis to identify key patterns.  

3. **Feature Engineering**  
   - Created **Health Risk Score** (medical history).  
   - Created **Lifestyle Risk Score** (physical activity, stress).  

4. **Multicollinearity Check**  
   - Used **Variance Inflation Factor (VIF)** to identify redundant features.  
   - Removed features causing high multicollinearity.  

5. **Model Development & Tuning**  
   - Baseline model: **Linear Regression**.  
   - Tuned **XGBoost Regressor** using **RandomizedSearchCV**.  
   - Achieved **99.2% accuracy (R²)** with best hyperparameters.  

6. **Model Deployment**  
   - Saved best model using **joblib**.  
   - Integrated with **Streamlit app** for real-time predictions.  

---

## Tech Stack  

- Python 3.11+  
- Streamlit (Frontend UI)  
- scikit-learn (Regression, preprocessing)  
- XGBoost (Gradient Boosting model)  
- Joblib (Model persistence)  
- Pandas & NumPy (Data processing)  


## Author
Created by **Devesh Singh (Demonforms)**  

---
