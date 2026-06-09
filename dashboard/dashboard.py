import streamlit as st
import pandas as pd
import os

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Smart Agriculture Dashboard",
    layout="wide"
)

# ==============================
# TITLE
# ==============================

st.title("🌱 IoT Smart Agriculture Monitoring Dashboard")

st.markdown("Real-Time Agriculture Monitoring & Irrigation Analytics")

# ==============================
# FILE PATH
# ==============================

file_path = "data/sensor_data.csv"

# ==============================
# CHECK FILE EXISTS
# ==============================

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    # ==============================
    # LATEST VALUES
    # ==============================

    latest = df.iloc[-1]

    st.subheader("📌 Current Sensor Status")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🌡 Temperature",
        f"{latest['temperature']} °C"
    )

    col2.metric(
        "💧 Humidity",
        f"{latest['humidity']} %"
    )

    col3.metric(
        "🌱 Soil Moisture",
        f"{latest['soil_moisture']} %"
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "☀ Light Intensity",
        f"{latest['light_intensity']} lux"
    )

    col5.metric(
        "🚰 Water Level",
        f"{latest['water_level']} %"
    )

    col6.metric(
        "⚙ Pump Status",
        latest['pump_status']
    )

    # ==============================
    # SENSOR TABLE
    # ==============================

    st.subheader("📋 Recent Sensor Readings")

    st.dataframe(df.tail(10))

    # ==============================
    # CHARTS
    # ==============================

    st.subheader("📈 Temperature Trend")

    st.line_chart(df["temperature"])

    st.subheader("💧 Humidity Trend")

    st.line_chart(df["humidity"])

    st.subheader("🌱 Soil Moisture Trend")

    st.line_chart(df["soil_moisture"])

    st.subheader("☀ Light Intensity Trend")

    st.line_chart(df["light_intensity"])

    st.subheader("🚰 Water Level Trend")

    st.line_chart(df["water_level"])

    # ==============================
    # ALERTS
    # ==============================

    st.subheader("🚨 Alerts")

    if latest["soil_moisture"] < 40:
        st.error("Low Soil Moisture Detected")

    if latest["temperature"] > 35:
        st.warning("High Temperature Alert")

    if latest["water_level"] < 20:
        st.error("Low Water Level Alert")

    # ==============================
    # ANALYTICS
    # ==============================

    st.subheader("📊 Analytics Summary")

    col7, col8, col9 = st.columns(3)

    col7.metric(
        "Average Temperature",
        f"{df['temperature'].mean():.2f} °C"
    )

    col8.metric(
        "Average Humidity",
        f"{df['humidity'].mean():.2f} %"
    )

    col9.metric(
        "Average Soil Moisture",
        f"{df['soil_moisture'].mean():.2f} %"
    )

    # ==============================
    # DOWNLOAD CSV
    # ==============================

    st.subheader("⬇ Download Sensor Data")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV File",
        data=csv,
        file_name="sensor_data.csv",
        mime="text/csv"
    )

else:

    st.error("sensor_data.csv not found")

    st.info("Run main.py first to generate sensor data")