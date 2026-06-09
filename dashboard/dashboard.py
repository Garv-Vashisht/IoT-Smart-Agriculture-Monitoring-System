import streamlit as st
import pandas as pd
import os

st.title("Smart Agriculture Dashboard")

file_path = "data/sensor_data.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    st.subheader("Recent Sensor Data")
    st.dataframe(df.tail(10))

    st.subheader("Temperature")
    st.line_chart(df["temperature"])

    st.subheader("Soil Moisture")
    st.line_chart(df["soil_moisture"])

    st.subheader("Humidity")
    st.line_chart(df["humidity"])

else:
    st.error("sensor_data.csv not found")
    st.info("Run main.py first")