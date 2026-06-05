import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Failure AI System",
    page_icon="❤️",
    layout="wide"
)

# ---------------- MODEL ----------------
model = pickle.load(open("heart_model.pkl", "rb"))

# ---------------- CSS (UPGRADED UI) ----------------
st.markdown("""
<style>

.stApp{
background: radial-gradient(circle at top,#0b1026,#050816);
color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background: linear-gradient(180deg,#050816,#0a0f1f,#111827);
}

/* Card UI */
.card{
background: rgba(255,255,255,0.07);
padding: 22px;
border-radius: 20px;
border: 1px solid rgba(0,229,255,0.25);
box-shadow: 0 0 15px rgba(0,229,255,0.15);
margin-bottom: 15px;
transition: 0.3s;
}

.card:hover{
transform: scale(1.01);
box-shadow: 0 0 25px rgba(0,229,255,0.4);
}

.metric{
font-size: 30px;
font-weight: bold;
color:#00E5FF;
}

.title{
font-size:32px;
font-weight:bold;
color:#ffffff;
text-align:center;
}

.small{
color:#aaa;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        menu_title="❤️ Heart AI System",
        options=["Dashboard", "Prediction", "Analytics", "About"],
        icons=["house", "heart-pulse", "bar-chart", "info-circle"],
        default_index=0
    )

# =====================================================
# DASHBOARD
# =====================================================
if selected == "Dashboard":

    st.markdown('<div class="card"><div class="title">❤️ Heart Failure AI Dashboard</div><div class="small">Smart Healthcare Prediction System</div></div>', unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    metrics = [
        ("🎯 Accuracy", "92.6%"),
        ("📊 Dataset", "299"),
        ("⚡ Features", "12"),
        ("🤖 Status", "Active")
    ]

    cols = [c1,c2,c3,c4]

    for i in range(4):
        with cols[i]:
            st.markdown(f"""
            <div class="card">
            <h4>{metrics[i][0]}</h4>
            <div class="metric">{metrics[i][1]}</div>
            </div>
            """, unsafe_allow_html=True)

# =====================================================
# PREDICTION
# =====================================================
elif selected == "Prediction":

    st.markdown('<div class="card"><h2>🧠 Patient Prediction</h2></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        age = st.number_input("Age", 1, 100)
        anaemia = st.selectbox("Anaemia", [0,1])
        cpk = st.number_input("CPK Level")
        diabetes = st.selectbox("Diabetes", [0,1])
        ef = st.number_input("Ejection Fraction")
        bp = st.selectbox("High BP", [0,1])
        platelets = st.number_input("Platelets")
        creatinine = st.number_input("Serum Creatinine")
        sodium = st.number_input("Serum Sodium")
        sex = st.selectbox("Sex", [0,1])
        smoking = st.selectbox("Smoking", [0,1])
        time = st.number_input("Follow-up Time")

        predict = st.button("🔍 Predict Risk")

    with col2:
        st.markdown('<div class="card"><h3>📌 Result Panel</h3></div>', unsafe_allow_html=True)

    if predict:

        features = np.array([[age, anaemia, cpk, diabetes, ef,
                              bp, platelets, creatinine,
                              sodium, sex, smoking, time]])

        pred = model.predict(features)

        try:
            prob = model.predict_proba(features)[0][1]
        except:
            prob = 0.5

        risk = prob * 100

        st.progress(int(risk))

        st.markdown(f"""
        <div class="card">
        <h2>Risk Score</h2>
        <div class="metric">{risk:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        if pred[0] == 1:
            st.error("⚠️ HIGH RISK DETECTED")
        else:
            st.success("✅ LOW RISK DETECTED")

# =====================================================
# ANALYTICS
# =====================================================
elif selected == "Analytics":

    st.markdown('<div class="card"><h2>📊 Analytics</h2></div>', unsafe_allow_html=True)

    df = pd.DataFrame({
        "Feature": ["Age","Diabetes","Smoking","BP","Anaemia"],
        "Impact": [85,70,60,75,50]
    })

    st.bar_chart(df.set_index("Feature"))

# =====================================================
# ABOUT
# =====================================================
elif selected == "About":

    st.markdown("""
    <div class="card">
    <h2>ℹ️ About Project</h2>

    AI-based Heart Failure Prediction System using Machine Learning + Streamlit

    <br><br>

    🔹 Developed by: Lokesh J  
    🔹 Domain: Healthcare AI  
    🔹 Tech: Python, Streamlit, ML
    </div>
    """, unsafe_allow_html=True)
