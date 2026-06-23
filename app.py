import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Credit Scorecard Dashboard", layout="centered")

st.title("🏦 Automated Credit Scorecard & Risk Grading")
st.write("Input the applicant's details below to calculate their credit score and default probability.")

st.sidebar.header("Applicant Features")

# 1. User Inputs (Matching your dataset features)
loan_amnt = st.sidebar.number_input("Loan Amount ($)", min_value=500, max_value=50000, value=10000, step=500)
funded_amnt_inv = st.sidebar.number_input("Funded Amount Investor ($)", min_value=500, max_value=50000, value=10000, step=500)
installment = st.sidebar.number_input("Monthly Installment ($)", min_value=10, max_value=2000, value=350, step=10)
annual_inc = st.sidebar.number_input("Annual Income ($)", min_value=5000, max_value=500000, value=60000, step=1000)
dti = st.sidebar.slider("Debt-to-Income Ratio (DTI)", min_value=0.0, max_value=50.0, value=15.0, step=0.1)
recoveries = st.sidebar.number_input("Recoveries ($)", min_value=0, max_value=50000, value=0)
collection_recovery_fee = st.sidebar.number_input("Collection Recovery Fee ($)", min_value=0, max_value=5000, value=0)

if st.button("Calculate Risk & Credit Score"):
    
    # 2. Simulated Probability of Default (PD) matching your logic constraints
    if recoveries > 0 or dti > 35:
        pd_prob = 0.85 
    else:
        pd_prob = 0.023 
        
    # 3. Scorecard Scaling Math (Exactly from your cells [126-128])
    BASE_SCORE = 600
    PDO = 50
    factor = PDO / np.log(2)
    offset = BASE_SCORE - factor * np.log(1)
    
    eps = 1e-10
    pd_adj = np.clip(pd_prob, eps, 1 - eps)
    odds = (1 - pd_adj) / pd_adj
    raw_credit_score = offset + factor * np.log(odds)
    
    # Scale strictly to your notebook's 300-900 bounds
    min_bound, max_bound = -1060.96, 1220.32
    credit_score_300_900 = 300 + (raw_credit_score - min_bound) * (600 / (max_bound - min_bound))
    credit_score_300_900 = int(np.clip(credit_score_300_900, 300, 900))
    
    # 4. Risk Grading (Exactly from your cell [129])
    if credit_score_300_900 <= 580:
        grade, color = "Very Poor", "🔴"
    elif credit_score_300_900 <= 670:
        grade, color = "Poor", "🟠"
    elif credit_score_300_900 <= 740:
        grade, color = "Fair", "🟡"
    elif credit_score_300_900 <= 800:
        grade, color = "Good", "🟢"
    else:
        grade, color = "Excellent", "🔵"
        
    # 5. UI Layout Output
    st.subheader("Results")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Credit Score", value=f"{credit_score_300_900} / 900")
    with col2:
        st.metric(label="Risk Grade", value=f"{color} {grade}")
    with col3:
        st.metric(label="Probability of Default (PD)", value=f"{pd_prob*100:.2f}%")
        
    st.progress((credit_score_300_900 - 300) / 600)
    
