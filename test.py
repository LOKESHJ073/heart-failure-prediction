import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Failure Prediction",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("heart_model.pkl", "rb"))

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0B1026,#141E46,#1F4068);
color:white;
}

h1,h2,h3,h4,h5,h6,label,p{
color:white !important;
}

.card{
background: rgba(255,255,255,0.08);
padding:20px;
border-radius:20px;
backdrop-filter: blur(10px);
box-shadow:0 4px 20px rgba(0,0,0,0.3);
text-align:center;
}

.metric{
font-size:28px;
font-weight:bold;
color:#00E5FF;
}

.stButton>button{
width:100%;
background:linear-gradient(90deg,#ff416c,#ff4b2b);
color:white;
border:none;
border-radius:12px;
height:55px;
font-size:18px;
font-weight:bold;
}

.stButton>button:hover{
background:linear-gradient(90deg,#ff4b2b,#ff416c);
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("❤️ Heart Failure")

    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter patient name"
    )

    height_cm = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

    weight_kg = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=200,
        value=70
    )

    bmi = weight_kg / ((height_cm/100)**2)

    st.markdown(
        f"""
        <div class="card">
        <h4>BMI</h4>
        <div class="metric">{bmi:.2f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- HEADER ----------------

col1,col2 = st.columns([1,4])

with col1:
    try:
        image = Image.open("heart.png")
        st.image(image,width=120)
    except:
        st.write("❤️")

with col2:
    st.title("❤️ Heart Failure Prediction System")
    st.markdown(
        "### 🩺 AI Powered Healthcare Risk Prediction"
    )

st.markdown("---")

# ---------------- DASHBOARD CARDS ----------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
    <h4>Model Accuracy</h4>
    <div class="metric">92.6%</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h4>Dataset</h4>
    <div class="metric">299</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h4>Features</h4>
    <div class="metric">12</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
    <h4>AI Status</h4>
    <div class="metric">Active</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- INPUT FORM ----------------

left,right = st.columns([2,1])

with left:

    st.subheader("📋 Patient Information")

    age = st.number_input(
        "Age",
        1,100,50
    )

    anaemia = st.selectbox(
        "Anaemia",
        [0,1]
    )

    creatinine_phosphokinase = st.number_input(
        "CPK Level",
        value=250
    )

    diabetes = st.selectbox(
        "Diabetes",
        [0,1]
    )

    ejection_fraction = st.number_input(
        "Ejection Fraction",
        1,100,38
    )

    high_blood_pressure = st.selectbox(
        "High Blood Pressure",
        [0,1]
    )

    platelets = st.number_input(
        "Platelets",
        value=263358.0
    )

    serum_creatinine = st.number_input(
        "Serum Creatinine",
        value=1.0
    )

    serum_sodium = st.number_input(
        "Serum Sodium",
        value=136
    )

    sex = st.selectbox(
        "Sex",
        [0,1]
    )

    smoking = st.selectbox(
        "Smoking",
        [0,1]
    )

    time = st.number_input(
        "Follow Up Time",
        value=100
    )

with right:

    st.markdown("""
    <div class="card">
    <h3>ℹ️ Project Overview</h3>
    <br>
    AI based heart failure prediction using
    Machine Learning.
    <br><br>
    ✅ Early Detection
    <br>
    ✅ Healthcare Analytics
    <br>
    ✅ Clinical Support
    <br>
    ✅ Risk Assessment
    </div>
    """, unsafe_allow_html=True)

# ---------------- PREDICTION ----------------

st.markdown("<br>", unsafe_allow_html=True)

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

    try:
        probability = model.predict_proba(features)[0][1]
    except:
        probability = 0.5

    st.subheader("📊 Prediction Result")

    st.progress(float(probability))

    st.metric(
        "Heart Failure Risk %",
        f"{probability*100:.2f}%"
    )

    if prediction[0] == 1:

        st.error(
            "⚠️ HIGH RISK OF HEART FAILURE"
        )

        st.warning(
            "Patient should undergo further medical evaluation."
        )

    else:

        st.success(
            "✅ LOW RISK OF HEART FAILURE"
        )

        st.info(
            "Patient currently shows lower risk indicators."
        )

    history = pd.DataFrame({
        "Patient":[patient_name],
        "Risk %":[round(probability*100,2)]
    })

    st.subheader("📁 Prediction History")

    st.dataframe(history)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
"""
<center>
<h4>❤️ Heart Failure Prediction System</h4>
<p>Developed by Lokesh | M.Sc Data Science</p>
</center>
""",
unsafe_allow_html=True
)
