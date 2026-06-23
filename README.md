# 🏦 Automated Bank Credit Scorecard & Risk Grading System

An end-to-end Machine Learning pipeline and interactive web application that automates credit risk assessment. The system processes historical loan application data, handles extreme class imbalances, trains predictive risk models, and translates raw default probabilities into a traditional **300–900 credit scoring scale** with corresponding official bank Risk Grades.

---

## 🚀 Live Demo
The application is wrapped in a dynamic UI built with **Streamlit** and securely exposed via a stable **Ngrok** tunnel link generated straight from the development environment.

---

## 🛠️ Project Architecture & Workflow

### 1. Data Processing & Feature Engineering
* **Data Cleaning:** Automatically parsed complex loan parameters (e.g., converting text-based terms like `' 36 months'` to integers, and percentage strings like `'10.65%'` to floats).
* **Missing Value Imputation:** Fixed incomplete applicant history using mean/median statistical imputations.
* **Categorical Encoding:** Leveraged One-Hot Encoding (`pd.get_dummies`) to translate non-numeric applicant profiles into machine-readable features.

### 2. Machine Learning Model Training
The project evaluates and balances multiple algorithms to find the optimal risk classifier:
* **Random Forest Classifier:** Achieved **99.5% accuracy** and an **AUC Score of 0.998**.
* **Support Vector Classifier (SVC):** Tuned via a linear kernel to reach **99.3% accuracy**.
* **Logistic Regression:** Reached **99.3% accuracy** and served as the foundational model for credit scorecard alignment.

### 3. Credit Scorecard Scaling (Industry Standard)
Instead of simply showing a raw binary prediction (0 or 1), the application applies real-world banking math using **Log-Odds** and **PDO (Points to Double the Odds)** logic:
* **Base Score:** 600 points when odds are 1:1.
* **PDO:** 50 points (the credit score increases by 50 points every time the applicant's risk odds halve).
* **Final Mapping:** Scaled bounds map smoothly onto a **300–900 scale**:
  * **900:** Impeccable credit (Virtually 0% Probability of Default).
  * **300:** Extreme credit risk (Near 100% Probability of Default).

---

## 📊 App Feature Metrics (Sidebar Inputs)
The interactive dashboard allows loan officers or applicants to input numeric features to generate a real-time risk certificate:
* **Financial Metrics:** Loan Amount requested, Funded Amount, and Monthly Installments.
* **Risk Ratios:** Annual Income and Debt-to-Income (DTI) ratio slider.
* **Loss Recovery Data:** Historic recoveries and collection recovery fees.

---

## 📦 Repository Structure

```text
📁 bank-credit-scorecard/
│
├── Bank_Credit_Scorecard_&_Risk_Grading_System.ipynb # Full Data Science notebook (EDA, Cleaning, ML Training, Math)
├── app.py                # Frontend dashboard user interface code (Streamlit)
├── requirements.txt      # Automated setup environment dependencies
└── README.md             # Project documentation and summary
