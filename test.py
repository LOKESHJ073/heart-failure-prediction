import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Heart Failure AI Dashboard",
    page_icon="❤️",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = pickle.load(open("heart_model.pkl", "rb"))

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#050816,#0B1026,#111827);
color:white;
}

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#050816,#0A0F1F,#111827);
}

h1,h2,h3,h4,h5,h6,p,label{
color:white !important;
}

.card{
background:rgba(255,255,255,0.08);
padding:20px;
border-radius:25px;
backdrop-filter:blur(20px);
border:1px solid rgba(0,229,255,0.4);
box-shadow:0 0 20px rgba(0,229,255,0.4);
transition:all 0.3s ease;
}

.card:hover{
transform:translateY(-5px);
box-shadow:0 0 30px rgba(255,0,128,0.6);
}
.metric{
font-size:32px;
font-weight:bold;
color:#00E5FF;
text-shadow:0 0 15px #00E5FF;
}


</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("# ❤️ Heart failure prediction")

    selected = option_menu(
        menu_title=None,
        options=[
            "Dashboard",
            "Prediction",
            "Analytics",
            "About"
        ],
        icons=[
            "house",
            "heart-pulse",
            "bar-chart",
            "info-circle"
        ],
        default_index=0
    )
# 1️⃣ SIDEBAR (ONLY MENU)
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Dashboard","Prediction","Analytics","About"],
        icons=["house","heart-pulse","bar-chart","info-circle"],
        default_index=0
    )

# 2️⃣ DASHBOARD PAGE
if selected == "Dashboard":
    st.title("Dashboard")

    # 👉 ALL dashboard cards here
    st.write("Dashboard content")

# 3️⃣ PREDICTION PAGE
elif selected == "Prediction":
    st.title("Prediction")

    # 👉 ALL input boxes + predict button here
    age = st.number_input("Age")
    st.write("Prediction UI here")

# 4️⃣ ANALYTICS PAGE
elif selected == "Analytics":
    st.title("Analytics")

    # 👉 charts here

# 5️⃣ ABOUT PAGE
elif selected == "About":
    st.title("About")
# ---------------- HEADER ----------------

st.markdown("""
<div class="card">
<h1>❤️ Heart Failure Prediction Dashboard</h1>
<p>AI Powered Healthcare Analytics System</p>
</div>
""", unsafe_allow_html=True)

st.write("")
# ---------------- TOP ANALYTICS ----------------

st.write("")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
        <h4>🎯 Accuracy</h4>
        <div class="metric">92.6%</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h4>📊 Dataset</h4>
        <div class="metric">299</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h4>⚡ Features</h4>
        <div class="metric">12</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
        <h4>🤖 AI Status</h4>
        <div class="metric">Active</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
left,right = st.columns([2,1])

with left:

    st.markdown("""
    <div class="card">
    <h2>🩺 Heart Failure Prediction System</h2>

    <br>

    This AI-powered system predicts heart failure risk
    using clinical patient information.

    <br><br>

    ✅ Early Risk Detection

    <br>

    ✅ Clinical Decision Support

    <br>

    ✅ Healthcare Analytics

    <br>

    ✅ Machine Learning Prediction

    </div>
    """, unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="card">
    <h3>📈 Quick Stats</h3>

    <br>

    Patients Analysed: 299

    <br><br>

    Features Used: 12

    <br><br>

    Model Accuracy: 92.6%

    <br><br>

    Prediction Engine: Active
    </div>
    """, unsafe_allow_html=True)
    # ---------------- PATIENT SECTION ----------------

st.write("")
st.markdown("## 📋 Patient Information")

col1,col2 = st.columns([2,1])

with col1:

    patient_name = st.text_input(
        "👤 Patient Name"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=50
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
        "Ejection Fraction (%)",
        min_value=1,
        max_value=100,
        value=38
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

with col2:

    st.markdown("""
    <div class="card">
    <h3>🧮 BMI Calculator</h3>
    </div>
    """, unsafe_allow_html=True)

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=250,
        value=170
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=200,
        value=70
    )

    bmi = weight / ((height/100)**2)

    st.markdown(
        f'''
        <div class="card">
        <h4>BMI Score</h4>
        <div class="metric">{bmi:.2f}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    if bmi < 18.5:
        st.warning("Underweight")

    elif bmi < 25:
        st.success("Normal Weight")

    elif bmi < 30:
        st.warning("Overweight")

    else:
        st.error("Obese")
        st.write("")

predict_btn = st.button(
    "🔍 Predict Heart Failure Risk"
)
# ---------------- PREDICTION ----------------

if predict_btn:

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
        probability = 0.50

    risk_score = probability * 100

    st.write("")
    st.markdown("## 📊 Prediction Results")

    r1,r2,r3 = st.columns(3)

    with r1:
        st.markdown(f"""
        <div class="card">
        <h4>🎯 Risk Score</h4>
        <div class="metric">{risk_score:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

    with r2:
        st.markdown(f"""
        <div class="card">
        <h4>👤 Patient</h4>
        <div class="metric">{patient_name}</div>
        </div>
        """, unsafe_allow_html=True)

    with r3:
        st.markdown(f"""
        <div class="card">
        <h4>🧮 BMI</h4>
        <div class="metric">{bmi:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.progress(risk_score / 100)

    if prediction[0] == 1:

        st.error("⚠️ HIGH RISK OF HEART FAILURE")

        st.markdown("""
        <div class="card">
        <h3>🚨 Medical Recommendation</h3>

        Immediate medical evaluation recommended.

        <br><br>

        • Consult a cardiologist

        <br>

        • Monitor blood pressure

        <br>

        • Regular health checkups

        <br>

        • Follow prescribed medication
        </div>
        """, unsafe_allow_html=True)

    else:

        st.success("✅ LOW RISK OF HEART FAILURE")

        st.markdown("""
        <div class="card">
        <h3>💚 Health Recommendation</h3>

        Patient currently shows lower risk indicators.

        <br><br>

        • Maintain healthy diet

        <br>

        • Exercise regularly

        <br>

        • Avoid smoking

        <br>

        • Regular health monitoring
        </div>
        """, unsafe_allow_html=True)
        # ---------------- ANALYTICS SECTION ----------------

st.write("")
st.markdown("## 📈 Health Analytics")

a1, a2 = st.columns(2)

with a1:

    st.markdown("""
    <div class="card">
    <h3>❤️ Risk Factors</h3>
    </div>
    """, unsafe_allow_html=True)

    risk_data = {
        "Feature":[
            "Age",
            "Diabetes",
            "Smoking",
            "Blood Pressure",
            "Anaemia"
        ],
        "Impact":[
            85,
            70,
            60,
            75,
            50
        ]
    }

    st.bar_chart(
        pd.DataFrame(risk_data).set_index("Feature")
    )

with a2:

    st.markdown("""
    <div class="card">
    <h3>📊 Patient Metrics</h3>
    </div>
    """, unsafe_allow_html=True)

    metric_data = {
        "Metric":[
            "BMI",
            "Sodium",
            "Creatinine"
        ],
        "Value":[
            bmi,
            serum_sodium,
            serum_creatinine
        ]
    }

    st.bar_chart(
        pd.DataFrame(metric_data).set_index("Metric")
    )

# ---------------- HISTORY ----------------

st.write("")
st.markdown("## 📁 Prediction History")

history_df = pd.DataFrame({
    "Patient":[patient_name],
    "Age":[age],
    "BMI":[round(bmi,2)],
    "Smoking":[smoking],
    "Diabetes":[diabetes]
})

st.dataframe(
    history_df,
    use_container_width=True
)

# ---------------- DEVELOPER CARD ----------------

st.write("")

d1,d2 = st.columns([2,1])

with d1:

    st.markdown("""
    <div class="card">
    <h3>🏥 About This Project</h3>

    AI Powered Heart Failure Prediction System
    developed using Machine Learning and Streamlit.

    <br><br>

    Features:

    <br>

    ✅ Heart Failure Prediction

    <br>

    ✅ BMI Analysis

    <br>

    ✅ Healthcare Dashboard

    <br>

    ✅ Risk Analytics

    <br>

    ✅ AI Based Decision Support

    </div>
    """, unsafe_allow_html=True)

with d2:

    st.markdown("""
    <div class="card">
    <h3>👨‍💻 Developer</h3>

    <br>

    Lokesh J

    <br><br>

    M.Sc Data Science

    <br><br>

    Final Year Project

    <br><br>

    Heart Failure Prediction System
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.write("")
st.markdown("---")

st.markdown("""
<div style='text-align:center'>

<h3>❤️ Heart Failure Prediction Dashboard</h3>

AI Powered Healthcare Analytics System

<br><br>

Developed by Lokesh J

<br>

M.Sc Data Science

</div>
""", unsafe_allow_html=True)
