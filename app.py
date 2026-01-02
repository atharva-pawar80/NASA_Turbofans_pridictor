import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="Jet Engine Health AI", layout="wide")

# --- CUSTOM CSS FOR JET THEME ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stMetric {
        background-color: #1a1c24;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #3e4556;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #3e4556;
        background-color: #1a1c24;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    return joblib.load('engine_model.pkl')

model = load_model()

# --- SIDEBAR: SENSOR INPUTS ---
st.sidebar.title("🛠️ Engine Telemetry")
st.sidebar.write("Adjust sensor inputs manually")

# We create sliders for all 21 sensors in the sidebar
sensor_values = []
for i in range(1, 22):
    # Set default values based on common NASA data ranges
    val = st.sidebar.slider(f"Sensor {i}", 0.0, 1000.0, 500.0)
    sensor_values.append(val)

# --- MAIN INTERFACE ---
st.title("✈️ NASA Turbofan Diagnostic System")
st.subheader("Predictive Maintenance AI Terminal")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📡 Current Status")
    if st.button("RUN DIAGNOSTIC SCAN"):
        input_data = np.array([sensor_values])
        prediction = int(model.predict(input_data)[0])
        
        # Display Result as a Metric
        if prediction < 30:
            st.metric("Estimated Remaining Life", f"{prediction} Cycles", delta="- Critical", delta_color="inverse")
            st.error("🚨 CRITICAL ALERT: Immediate grounding required.")
        elif prediction < 100:
            st.metric("Estimated Remaining Life", f"{prediction} Cycles", delta="- Warning", delta_color="normal")
            st.warning("⚠️ MAINTENANCE REQUIRED: High wear detected.")
        else:
            st.metric("Estimated Remaining Life", f"{prediction} Cycles", delta="Optimal")
            st.success("✅ ENGINE HEALTHY: Systems within normal parameters.")

with col2:
    st.markdown("### 📈 Logic & Insights")
    st.info("""
    **Model Logic:** This AI uses a Random Forest Regressor to analyze non-linear degradation patterns across 21 sensors simultaneously. 
    
    **Key Parameter:** Sensor 11 (Heat) and Sensor 9 (Pressure) are currently the highest weighted variables in this diagnostic.
    """)

# Add a decorative aircraft icon at the bottom
st.markdown("---")
st.markdown("<p style='text-align: center; color: #3e4556;'>NASA C-MAPSS Dataset Analysis Terminal v1.0</p>", unsafe_allow_html=True)
