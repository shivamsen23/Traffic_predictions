import streamlit as st
import numpy as np
import pickle
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Traffic Prediction System",
    page_icon="🚦",
    layout="centered"
)

# ================= LOAD MODEL =================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ================= SESSION STATE =================
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# ================= BACKGROUND =================
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        header[data-testid="stHeader"] {{ display: none; }}
        footer {{ display: none; }}

        .stApp {{
            background:
                linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}

        /* Card */
        .card {{
            background: rgba(15,15,15,0.95);
            border-radius: 16px;
            padding: 24px;
            color: white;
            max-width: 420px;
            margin: auto;
            box-shadow: 0 20px 40px rgba(0,0,0,0.7);
        }}

        /* Mobile responsive */
        @media (max-width: 600px) {{
            .card {{
                width: 92%;
                padding: 20px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("traffic_bg.avif")

# ================= MAIN CARD =================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    '<h2 style="text-align:center; color:white;">🚦 Traffic Prediction</h2>',
    unsafe_allow_html=True
)
st.markdown(
    '<p style="text-align:center; color:#cbd5e1;">Predict vehicle count using Machine Learning</p>',
    unsafe_allow_html=True
)
st.markdown("""
<style>
/* ---------- LABEL TEXT (Junction, Hour, Day, etc.) ---------- */
label {
    color: white !important;
    font-weight: 600;
}

/* ---------- SELECTBOX (selected value text) ---------- */
div[data-baseweb="select"] > div {
    color: white !important;
    background-color: rgba(0,0,0,0.45) !important;
    border-radius: 8px;
}

/* ---------- SELECTBOX DROPDOWN ---------- */
ul[role="listbox"] {
    background-color: #0f172a !important;
}

/* Dropdown options text */
li[role="option"] {
    color: black !important;   /* readable */
}

/* Hover option */
li[role="option"]:hover {
    background-color: #1e293b !important;
    color: white !important;
}

/* ---------- SLIDER VALUE TEXT ---------- */
div[data-testid="stSlider"] span {
    color: white !important;
    font-weight: 600;
}

/* ---------- SLIDER TRACK ---------- */
div[data-testid="stSlider"] > div {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

junction = st.selectbox("🚏 Junction", [1, 2, 3, 4])
hour = st.slider("🕒 Hour", 0, 23)
day = st.slider("📅 Day", 1, 31)
month = st.selectbox("📆 Month", list(range(1, 13)))
dayofweek = st.selectbox(
    "📍 Day of Week",
    range(7),
    format_func=lambda x: ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][x]
)

if st.button("🚗 Predict Traffic", use_container_width=True):
    X = np.array([[junction, hour, day, month, dayofweek]])
    X = scaler.transform(X)
    pred = model.predict(X)

    st.session_state.prediction_value = int(pred[0])
    st.session_state.show_result = True
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ================= RESULT POPUP (CENTERED & RESPONSIVE) =================
if st.session_state.show_result:
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown(
            '<h3 style="text-align:center; color:white; width:100%">🚦 Traffic Prediction Result</h3>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<h1 style="text-align:center; color:white; margin-top:-25px;">🚘 {st.session_state.prediction_value}</h1>',
            unsafe_allow_html=True
        )

        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.show_result = False
            st.rerun()
