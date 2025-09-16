import streamlit as st
import joblib
import pandas as pd
import shap
import matplotlib.pyplot as plt

# Load trained model and features
@st.cache_resource
def load_model():
    model = joblib.load("xgb_model.pkl")
    features = joblib.load("xgb_features.pkl")
    return model, features

xgb_model, feature_names = load_model()


# Streamlit App UI
st.title("Credit Fraud / Loan Default Prediction")
st.write("Enter applicant details to predict default/fraud risk and explain the decision.")

# Example features — adjust based on your dataset
numeric_inputs = {
    "loan_amnt": st.number_input("Loan Amount ($)", min_value=500, max_value=50000, value=10000, step=500),
    "int_rate": st.number_input("Interest Rate (%)", min_value=5.0, max_value=40.0, value=12.0, step=0.1),
    "annual_inc": st.number_input("Annual Income ($)", min_value=5000, max_value=500000, value=60000, step=1000),
    "dti": st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=50.0, value=15.0, step=0.1),
    "revol_util": st.number_input("Revolving Credit Utilization (%)", min_value=0.0, max_value=150.0, value=30.0, step=0.1),
    "total_acc": st.number_input("Total Credit Accounts", min_value=1, max_value=100, value=20, step=1),
}

categorical_inputs = {
    "term": st.selectbox("Loan Term", ["36 months", "60 months"]),
    "grade": st.selectbox("Loan Grade", ["A","B","C","D","E","F","G"]),
    "sub_grade": st.selectbox("Sub Grade", ["A1","A2","A3","B1","B2","C1","C2","D1","D2"]),
    "emp_length": st.selectbox("Employment Length", ["< 1 year","1 year","2 years","5 years","10+ years"]),
    "home_ownership": st.selectbox("Home Ownership", ["RENT","MORTGAGE","OWN"]),
    "purpose": st.selectbox("Loan Purpose", ["credit_card","car","debt_consolidation","home_improvement","small_business","other"]),
}

# Predict button

if st.button("Predict Risk"):
# Create a single-row dataframe
    input_data = {**numeric_inputs, **categorical_inputs}
    input_df = pd.DataFrame([input_data])

# One-hot encode using feature names from training
    input_encoded = pd.get_dummies(input_df)
    input_encoded = input_encoded.reindex(columns=feature_names, fill_value=0)

# Predict
    prob = xgb_model.predict_proba(input_encoded)[0,1]
    prediction = "HIGH RISK (Fraud/Default)" if prob >= 0.5 else "LOW RISK (Safe)"

    st.subheader("Prediction Result")
    st.write(f"**{prediction}**")
    st.write(f"Predicted Probability of Default/Fraud: **{prob:.2f}**")

# SHAP Explainability
    st.subheader("Feature Contribution (SHAP Explanation)")
    explainer = shap.TreeExplainer(xgb_model)
    shap_values = explainer(input_encoded)

# Plot SHAP values for this individual
    fig, ax = plt.subplots()
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig)
