import streamlit as st
import pandas as pd
import joblib

# Load model and features
xgb = joblib.load("xgb_model.pkl")
features = joblib.load("xgb_features.pkl")

st.title("Anti-Money Laundering Detection App")
st.write("This app predicts whether a financial transaction is **suspicious** or **normal**.")

#Demo Transactions
demo_transactions = {
    "Normal Transaction": {
        "loan_amnt": 8000, "term": 36, "Int Rate": 10.0, "Grade": "B", "Sub Grade": "B3",
        "emp_length": "5 years", "Home Ownership": "MORTGAGE", "Annual Inc": 60000,
        "purpose": "Debt Consolidation", "dti": 15.0, "Revol Util": 40.0, "Total Acc": 20
    },
    "Suspicious Transaction": {
        "loan_amnt": 50000, "term": 60, "int_rate": 28.0, "grade": "G", "sub_grade": "G5",
        "emp_length": "< 1 year", "Home Ownership": "RENT", "Annual Inc": 12000,
        "purpose": "Small Business", "dti": 45.0, "Revol Util": 120.0, "Total Acc": 5
    }
}

mode = st.radio("Choose Input Mode", ["Manual Input", "Demo Mode"])

#Manual Input
if mode == "Manual Input":
    loan_amnt = st.number_input("Loan Amount($)", min_value=100, max_value=500000, value=10000, step=100)
    term = st.selectbox("Term (months)", [36, 60])
    int_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=40.0, value=10.5, step=0.1)
    grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
    sub_grade = st.selectbox("Loan Sub-grade", [f"{g}{i}" for g in "ABCDEFG" for i in range(1, 6)])
    emp_length = st.selectbox("Employment Length", ["< 1 year", "1 year", "2 years", "3 years", "4 years",
                                                    "5 years", "6 years", "7 years", "8 years", "9 years", "10+ years"])
    home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE", "OTHER"])
    annual_inc = st.number_input("Annual Income", min_value=1000, max_value=1000000, value=50000, step=1000)
    purpose = st.selectbox("Loan Purpose", [
        "debt_consolidation", "Credit Card", "Home Improvement", "Major Purchase", "Small Business",
        "car", "medical", "moving", "vacation", "wedding", "house", "renewable_energy", "educational", "other"
    ])
    dti = st.number_input("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)
    revol_util = st.number_input("Revolving Credit Utilization (%)", min_value=0.0, max_value=150.0, value=50.0, step=0.1)
    total_acc = st.number_input("Total Accounts", min_value=1, max_value=200, value=15, step=1)

    input_data = pd.DataFrame([{
        "loan_amnt": loan_amnt, "term": term, "int_rate": int_rate, "grade": grade,
        "sub_grade": sub_grade, "emp_length": emp_length, "home_ownership": home_ownership,
        "annual_inc": annual_inc, "purpose": purpose, "dti": dti,
        "revol_util": revol_util, "total_acc": total_acc
    }])

#Demo Input
else:
    demo_choice = st.selectbox("Select a Demo Transaction", list(demo_transactions.keys()))
    input_data = pd.DataFrame([demo_transactions[demo_choice]])
    st.write("### Selected Transaction:")
    st.write(input_data)

#Match features
input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=features, fill_value=0)

#Predict
if st.button("Predict"):
    prob = xgb.predict_proba(input_data)[:, 1][0]
    pred = int(prob >= 0.5)

    st.subheader("Prediction Result")
    st.write(f"**Suspicion Score:** {prob:.2f}")
    st.write(f"**Prediction:** {'Suspicious Transaction' if pred else 'Normal Transaction'}")
