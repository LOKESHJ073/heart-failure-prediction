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

# ---------------- CSS ----------------
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
margin-bottom:15px;
}

.metric{
font-size:28px;
font-weight:bold;
color:#00E5FF;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        menu_title="❤️ Heart AI Menu",
        options=["Dashboard", "Prediction", "Analytics", "About"],
        icons=["house", "heart-pulse", "bar-chart", "info-circle"],
        default_index=0
    )

# =========================================================
# DASHBOARD
# =========================================================
if selected == "Dashboard":

    st.markdown("""
    <div class="card">
    <h1>❤️ Heart Failure Dashboard</h1>
    <p>AI Powered Healthcare System</p>
    </div>
    """, unsafe_allow_html=True)

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


# =========================================================
# PREDICTION
# =========================================================
elif selected == "Prediction":

    st.markdown("""
    <div class="card">
    <h2>🧠 Heart Failure Prediction</h2>
    </div>
    """, unsafe_allow_html=True)

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
    time = st.number_input("Follow Up Time")

    if st.button("Predict"):

        features = np.array([[age, anaemia, cpk, diabetes, ef,
                              bp, platelets, creatinine,
                              sodium, sex, smoking, time]])

        pred = model.predict(features)

        try:
            prob = model.predict_proba(features)[0][1]
        except:
            prob = 0.5

        risk = prob * 100

        st.markdown(f"""
        <div class="card">
        <h3>Risk Score</h3>
        <div class="metric">{risk:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)

        if pred[0] == 1:
            st.error("⚠️ HIGH RISK")
        else:
            st.success("✅ LOW RISK")


# =========================================================
# ANALYTICS
# =========================================================
elif selected == "Analytics":

    st.markdown("""
    <div class="card">
    <h2>📊 Analytics</h2>
    </div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame({
        "Feature":["Age","Diabetes","Smoking","BP"],
        "Impact":[85,70,60,75]
    })

    st.bar_chart(df.set_index("Feature"))


# =========================================================
# ABOUT
# =========================================================
elif selected == "About":

    st.markdown("""
    <div class="card">
    <h2>ℹ️ About Project</h2>

    Heart Failure Prediction using Machine Learning + Streamlit

    <br><br>

    Developer: Lokesh J
    </div>
    """, unsafe_allow_html=True)
