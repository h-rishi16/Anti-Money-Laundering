# Anti–Money Laundering (AML) Transaction Monitoring

## Overview
This project predicts suspicious and potentially illicit transactions using historical financial data and machine learning. The goal is to help banks and fintechs automate AML compliance, flag high-risk transactions, and provide transparency for regulatory audits.

Two models are developed:
- Logistic Regression – interpretable baseline
- XGBoost – advanced, high-performance model

SHAP values are leveraged to explain model decisions and identify key transaction risk factors.

## Business Problem
Money laundering is a critical risk for financial institutions, leading to regulatory fines and reputational damage. An effective AML system should:
- Detect suspicious transactions in real time
- Minimize false negatives (missed laundering attempts)
- Provide clear, explainable risk scores for compliance teams

## Tech Stack
- Python (Pandas, Numpy)
- Scikit-learn (Logistic Regression)
- XGBoost (gradient boosting for tabular data)
- SHAP (explainable AI)
- Jupyter Notebook
- Streamlit (for interactive web app)

## Dataset
- Source: Synthetic or anonymized transaction data
- Features: amount, type, country, customer ID, timestamp, engineered features (velocity, anomalies, geo risk, customer profile)
- Target:
  - 1 → Suspicious Transaction
  - 0 → Legitimate Transaction

## Project Pipeline
**1. Data Preparation**
- Data cleaning and preprocessing (remove irrelevant fields, handle missing values, encode categoricals)
- Feature engineering: transaction velocity, anomaly scores, geo risk, customer patterns

**2. Exploratory Data Analysis (EDA)**
- Analyze distribution of flagged transactions
- Identify trends based on amount, country, time, and customer segment
- Correlation and risk factor analysis

**3. Modeling**
- Logistic Regression (baseline, interpretable)
- XGBoost (handles class imbalance, achieves high recall and precision)

**4. Model Explainability**
- SHAP summary plots to highlight top risk drivers (amount, frequency, geo risk)
- Local explanations for individual flagged transactions

## Results
**Logistic Regression**
- ROC-AUC: ~0.98
- Good baseline interpretability

**XGBoost**
- ROC-AUC: ~0.99–1.00
- Excellent recall for suspicious transactions

**SHAP Insights**
- Top predictors: transaction amount, frequency, destination country, customer pattern

## Repository Structure
```
Anti-Money-Laundering/
│── AML_Notebook.ipynb              # Main notebook: EDA, preprocessing, modeling, explainability
│── app.py                          # Streamlit web app for transaction scoring and explanations
│── xgb_model.pkl                   # Trained XGBoost model
│── xgb_features.pkl                # Feature list used in model
│── README.md                       # Project documentation
│── requirements.txt                # Dependencies
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
- Input transaction details (amount, country, type, etc.)
- Get a prediction: **Suspicious** or **Legitimate**
- View SHAP explanations for each prediction

## Skills Demonstrated
- Data cleaning and feature engineering for AML
- Handling imbalanced classes and rare events in fraud detection
- Model evaluation (ROC-AUC, recall, F1)
- Explainable AI with SHAP values
- Saving/loading models with joblib
- Deploying ML apps via Streamlit

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
- Hyperparameter optimization (GridSearchCV, Optuna)
- Additional models (LightGBM, CatBoost, deep learning)
- Real-time scoring API for production deployment
- Integration with core banking or payment systems
- Enhanced risk profiling using external lists (e.g. OFAC, PEP)
- Scenario-based testing for new laundering typologies

## Author
Hrishikesh Joshi

---

## Appendix: Adapting AML Systems for Local and Global Compliance

### 1. Regulatory Relevance
- Complies with global AML standards (FATF) and can be adapted to local (e.g., RBI, FinCEN) regulations

### 2. Feature Engineering for Local Contexts
- Add KYC-based features, regional risk factors, and sector-specific red flags for local adaptation

### 3. Deployment Considerations
- Streamlit app can be integrated into compliance or transaction monitoring workflows
- Model explanations support regulatory audits and internal investigations

---

**In summary:**  
This project demonstrates an end-to-end, explainable workflow for AML transaction monitoring. The pipeline is adaptable for different regulatory environments and financial institutions, enhancing compliance and risk management.
