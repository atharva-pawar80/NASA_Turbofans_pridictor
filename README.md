# ✈️ Jet Engine Predictive Maintenance System
An AI-powered diagnostic tool built using the **NASA C-MAPSS dataset** to predict the **Remaining Useful Life (RUL)** of turbofan engines.

## 📊 Key Results
- **Algorithm:** Random Forest Regressor
- **Accuracy (RMSE):** 41.19 Cycles
- **Top Indicator:** Sensor 11 (Static Pressure/Heat)

## 🛠️ How it Works
1. **Data:** 21 sensors tracking engine health over time.
2. **Analysis:** Identified degradation trends in heat and pressure sensors.
3. **AI:** A model trained to recognize the "fingerprint" of an engine nearing failure.
4. **App:** A Streamlit interface for real-time diagnostics.

## 🚀 Setup
Run the app locally:
```bash
pip install -r requirements.txt
streamlit run app.py