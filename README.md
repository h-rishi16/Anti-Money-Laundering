# Anti–Money Laundering (AML) Transaction Monitoring

## Overview
This project uses machine learning to detect suspicious financial transactions that may indicate money laundering or other illicit activities. The solution is designed to help financial institutions comply with AML regulations, automate detection, and provide transparency for compliance teams.

We developed:
- Logistic Regression – interpretable baseline model
- XGBoost – advanced model with strong predictive power

Model explainability is achieved using SHAP, highlighting key risk factors in transaction monitoring.

## Business Problem
Money laundering is a major compliance and reputational risk for banks and fintechs. Regulatory frameworks require robust AML systems to:
- Detect and flag suspicious activity in real time
- Reduce false negatives (missed money laundering cases)
- Provide clear explanations for risk decisions, supporting regulatory audits

## Tech Stack
- Python (Pandas, Numpy)
- Scikit-learn (Logistic Regression, pipelines)
- XGBoost (gradient boosting)
- SHAP (model explainability)
- Jupyter Notebook
- Streamlit (interactive web app)

## Data
- Synthetic or anonymized transaction records
- Features: transaction amount, type, country, customer ID, timestamp, and engineered risk features (velocity, anomalies, geo-risk, customer profile)
- Target:
  - 1 → Suspicious (potential money laundering)
  - 0 → Legitimate

## Project Pipeline
**1. Data Preparation**
- Cleaned and preprocessed transaction data
- Engineered AML-specific risk features: velocity, anomalies, geo-risk, customer patterns

**2. Exploratory Data Analysis (EDA)**
- Distribution of suspicious/legit transactions
- Patterns by geography, amount, customer segments

**3. Modeling**
- Logistic Regression (baseline, ROC-AUC ~0.98)
- XGBoost (advanced, ROC-AUC ~0.99–1.00)
- Emphasis on recall (minimizing missed suspicious cases)

**4. Model Explainability**
- SHAP identifies top risk drivers: amount, frequency, risky destinations
- Global and local explanations for compliance

## Results
- **Logistic Regression**: ROC-AUC ~0.98
- **XGBoost**: ROC-AUC ~0.99–1.00
- **SHAP Insights**: Transaction amount, frequency, destination country are top indicators

## Repository Structure
```
Anti-Money-Laundering/
│── AML_Notebook.ipynb              # Jupyter Notebook: EDA, modeling, SHAP
│── app.py                          # Streamlit app for transaction risk scoring
│── xgb_model.pkl                   # Trained XGBoost model
│── xgb_features.pkl                # Feature list
│── requirements.txt                # Dependencies
│── README.md                       # Project documentation
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/h-rishi16/Anti-Money-Laundering.git
   cd Anti-Money-Laundering
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook:
   ```bash
   jupyter notebook AML_Notebook.ipynb
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Web App Usage
- Enter transaction details (amount, country, frequency, etc.)
- The app predicts whether a transaction is **Suspicious** or **Legitimate**, and explains the risk score with SHAP.

## Skills Demonstrated
- Data cleaning and feature engineering for AML
- Handling class imbalance and rare events
- Model training and evaluation (ROC-AUC, recall)
- Model explainability with SHAP
- Deploying ML models with Streamlit

## Dependencies
```
pandas
numpy
scikit-learn
xgboost
shap
jupyter
streamlit
joblib
```

## Future Work
- Hyperparameter tuning (GridSearchCV, Optuna)
- Additional models (Random Forest, LightGBM)
- Real-time transaction scoring API
- Integration with core banking or fintech platforms
- Enhanced geo-risk profiling (OFAC lists, high-risk countries)
- Adapting models to new regulatory requirements

## Author
Hrishikesh Joshi

---

## Appendix: Adapting AML Detection to India and Global Compliance

### 1. Regulatory Context
- Aligns with global AML guidelines (FATF) and Indian regulations (PMLA, RBI AML standards)
- Adaptable to other geographies with country-specific rules

### 2. Data Sources for Indian/Global AML
- RBI, FIU-IND, or bank-provided transaction datasets (India)
- Public data on sanctioned entities, high-risk geographies
- Synthetic data or Kaggle AML datasets for prototyping

### 3. Feature Engineering for Local Compliance
- Incorporate KYC (Aadhaar, PAN in India), high-cash-risk regions, sectoral risks (e.g., jewelry, real estate)
- Dynamic risk scoring for new typologies

### 4. Deployment & Audit-readiness
- Explainable predictions for audit trails
- Modular pipeline for integration with transaction monitoring systems

---

**In summary:**  
This project demonstrates a robust, explainable workflow for AML transaction monitoring. The methods and pipeline can be adapted to meet regulatory requirements in India or globally, enhancing compliance and risk mitigation for banks and fintechs.
