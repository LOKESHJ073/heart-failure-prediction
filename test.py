import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("heart_model.pkl", "rb"))

# Page Configuration
st.set_page_config(
    page_title="Heart Failure Prediction",
    page_icon="❤️",
    layout="wide"
)

# Title
st.title("❤️ Heart Failure Prediction System")

st.markdown("""
### 🩺 Heart Failure Risk Prediction
Enter patient details below and click **Predict** to check the risk of heart failure.
""")

st.markdown("---")

# Two Column Layout
col1, col2 = st.columns([2, 1])

# Left Side - Input Form
with col1:

    st.subheader("📋 Patient Information")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=50
    )

    anaemia = st.selectbox(
        "Anaemia (0 = No, 1 = Yes)",
        [0, 1]
    )

    creatinine_phosphokinase = st.number_input(
        "CPK Level",
        min_value=0,
        value=250
    )

    diabetes = st.selectbox(
        "Diabetes (0 = No, 1 = Yes)",
        [0, 1]
    )

    ejection_fraction = st.number_input(
        "Ejection Fraction (%)",
        min_value=1,
        max_value=100,
        value=38
    )

    high_blood_pressure = st.selectbox(
        "High Blood Pressure (0 = No, 1 = Yes)",
        [0, 1]
    )

    platelets = st.number_input(
        "Platelets",
        min_value=10000.0,
        value=263358.0
    )

    serum_creatinine = st.number_input(
        "Serum Creatinine",
        min_value=0.1,
        value=1.0
    )

    serum_sodium = st.number_input(
        "Serum Sodium",
        min_value=100,
        max_value=150,
        value=136
    )

    sex = st.selectbox(
        "Sex (0 = Female, 1 = Male)",
        [0, 1]
    )

    smoking = st.selectbox(
        "Smoking (0 = No, 1 = Yes)",
        [0, 1]
    )

    time = st.number_input(
        "Follow Up Time (Days)",
        min_value=1,
        max_value=300,
        value=100
    )

# Right Side - Project Details
with col2:

    st.subheader("ℹ️ Project Overview")

    st.info("""
    Heart Failure Prediction System uses Machine Learning
    to predict heart failure risk based on patient data.
    """)

    st.success("""
    ✅ Early Risk Detection

    ✅ Clinical Decision Support

    ✅ Patient Monitoring

    ✅ Healthcare Analytics
    """)

    st.subheader("👨‍🎓 Developer")

    st.write("""
    **Lokesh**

    Final Year M.Sc Data Science
    """)

st.markdown("---")

# Prediction Button
if st.button("🔍 Predict Heart Failure Risk"):

    features = np.array([[
        age,
        anaemia,
        creatinine_phosphokinase,
        diabetes,
        ejection_fraction,
        high_blood_pressure,
        platelets,
        serum_creatinine,
        serum_sodium,
        sex,
        smoking,
        time
    ]])

    prediction = model.predict(features)

    st.subheader("📊 Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Failure")
        st.warning(
            "Patient should undergo further medical evaluation."
        )
    else:
        st.success("✅ Low Risk of Heart Failure")
        st.info(
            "Patient currently shows lower risk indicators."
        )

st.markdown("---")

# About Project
st.subheader("ℹ️ About Project")

st.write("""
This Heart Failure Prediction System uses Machine Learning
to predict the likelihood of heart failure based on
patient clinical records.

The model helps in:
• Early Risk Detection

• Clinical Decision Support

• Improved Patient Monitoring

• Healthcare Prediction Analysis
""")

st.markdown("---")

# Footer
st.caption("❤️ Heart Failure Prediction System")
st.caption("👨‍🎓 Developed by Lokesh")
st.caption("🎓 Final Year M.Sc Data Science Project")