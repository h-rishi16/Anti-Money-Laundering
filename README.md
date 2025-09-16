# Anti–Money Laundering (AML) Transaction Monitoring

This project applies machine learning to detect suspicious financial transactions that may indicate money laundering or other illicit activities. AML systems are a regulatory requirement for banks under FATF, EU AML directives, and the US Patriot Act.

---

## Project Structure

```
Project3_AML/
├── AML_Notebook.ipynb   # Jupyter Notebook (data prep, modeling, SHAP explainability)
├── app.py               # Streamlit app for transaction risk scoring
├── xgb_model.pkl        # Trained XGBoost model
├── xgb_features.pkl     # Feature list
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## Workflow

1. Data Preprocessing
   - Cleaned transaction data: amount, type, country, customer ID, timestamp
   - Engineered risk features:
     - Transaction velocity (frequency)
     - Transaction amount anomalies
     - Geographic risk indicators
     - Customer profile patterns

2. Modeling
   - Baseline: Logistic Regression (~0.70 ROC-AUC)
   - Advanced: XGBoost (~0.75–0.80 ROC-AUC)

3. Evaluation
   - Metrics: Precision, Recall, F1, ROC-AUC
   - Strong focus on recall to minimize missed suspicious cases

4. Explainability (SHAP)
   - Global feature importance
   - Local explanations (why a single transaction was flagged)

5. Deployment
   - Interactive Streamlit app for compliance teams to test transactions
   - Provides both prediction and explanation of risk factors

---

## Results

- Logistic Regression ROC-AUC: ~0.98
- XGBoost ROC-AUC: ~0.99–1.00
- SHAP identified transaction amount, frequency, and risky destinations as top risk indicators.

---

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Notebook

```bash
jupyter notebook AML_Notebook.ipynb
```

### 3. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## Conclusion

This project demonstrates how machine learning can enhance AML transaction monitoring systems by:
- Automating suspicious activity detection
- Explaining red flags using SHAP
- Providing an interactive tool for compliance officers

It completes the banking risk analytics portfolio by covering compliance and regulatory risk alongside credit and fraud risk.
