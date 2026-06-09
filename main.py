import random
import pandas as pd
from datetime import datetime
import time
import os
import matplotlib.pyplot as plt

# ==============================
# CREATE ALL REQUIRED FOLDERS
# ==============================

folders = [
    "data",
    "outputs",
    "images",
    "docs",
    "dashboard",
    "python_simulation",
    "circuit_diagram",
    "arduino_code"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# ==============================
# FILE PATHS
# ==============================

DATA_FILE = "data/sensor_data.csv"
ALERT_FILE = "outputs/alerts.txt"
REPORT_FILE = "docs/system_report.txt"

# ==============================
# THRESHOLDS
# ==============================

SOIL_THRESHOLD = 40
TEMP_THRESHOLD = 35
WATER_LEVEL_THRESHOLD = 20

# ==============================
# SENSOR DATA GENERATION
# ==============================

def generate_sensor_data():

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "soil_moisture": random.randint(20, 90),
        "temperature": random.randint(20, 45),
        "humidity": random.randint(30, 90),
        "light_intensity": random.randint(100, 1000),
        "water_level": random.randint(10, 100)
    }

# ==============================
# IRRIGATION LOGIC
# ==============================

def irrigation_logic(data):

    pump_status = "OFF"
    alerts = []

    if data["soil_moisture"] < SOIL_THRESHOLD:
        pump_status = "ON"
        alerts.append("Low Soil Moisture Detected")

    if data["temperature"] > TEMP_THRESHOLD:
        alerts.append("High Temperature Alert")

    if data["water_level"] < WATER_LEVEL_THRESHOLD:
        alerts.append("Low Water Level Alert")

    return pump_status, alerts

# ==============================
# SAVE SENSOR DATA
# ==============================

def save_data(data, pump_status):

    data["pump_status"] = pump_status

    df = pd.DataFrame([data])

    if os.path.exists(DATA_FILE):
        old_df = pd.read_csv(DATA_FILE)
        df = pd.concat([old_df, df], ignore_index=True)

    df.to_csv(DATA_FILE, index=False)

# ==============================
# SAVE ALERTS
# ==============================

def save_alerts(alerts):

    if alerts:
        with open(ALERT_FILE, "a") as file:

            for alert in alerts:
                file.write(f"{datetime.now()} -> {alert}\n")

# ==============================
# GENERATE REPORT
# ==============================

def generate_report():

    if not os.path.exists(DATA_FILE):
        return

    df = pd.read_csv(DATA_FILE)

    report = f"""
SMART AGRICULTURE SYSTEM REPORT
================================

Total Records: {len(df)}

Average Temperature: {df['temperature'].mean():.2f} °C
Average Humidity: {df['humidity'].mean():.2f} %
Average Soil Moisture: {df['soil_moisture'].mean():.2f} %
Average Water Level: {df['water_level'].mean():.2f} %

Pump ON Count:
{(df['pump_status'] == 'ON').sum()}

Pump OFF Count:
{(df['pump_status'] == 'OFF').sum()}
"""

    with open(REPORT_FILE, "w") as file:
        file.write(report)

# ==============================
# GENERATE CHARTS
# ==============================

def generate_charts():

    if not os.path.exists(DATA_FILE):
        return

    df = pd.read_csv(DATA_FILE)

    # Temperature Chart
    plt.figure(figsize=(10,5))
    plt.plot(df["temperature"])
    plt.title("Temperature Trend")
    plt.xlabel("Reading")
    plt.ylabel("Temperature")
    plt.savefig("images/temperature_chart.png")
    plt.close()

    # Soil Moisture Chart
    plt.figure(figsize=(10,5))
    plt.plot(df["soil_moisture"])
    plt.title("Soil Moisture Trend")
    plt.xlabel("Reading")
    plt.ylabel("Soil Moisture")
    plt.savefig("images/soil_moisture_chart.png")
    plt.close()

    # Humidity Chart
    plt.figure(figsize=(10,5))
    plt.plot(df["humidity"])
    plt.title("Humidity Trend")
    plt.xlabel("Reading")
    plt.ylabel("Humidity")
    plt.savefig("images/humidity_chart.png")
    plt.close()

# ==============================
# MAIN SYSTEM
# ==============================

def main():

    print("\nSMART AGRICULTURE MONITORING SYSTEM STARTED\n")

    while True:

        sensor_data = generate_sensor_data()

        pump_status, alerts = irrigation_logic(sensor_data)

        save_data(sensor_data, pump_status)

        save_alerts(alerts)

        generate_report()

        generate_charts()

        print("===================================")
        print(f"Time: {sensor_data['timestamp']}")
        print(f"Soil Moisture: {sensor_data['soil_moisture']}%")
        print(f"Temperature: {sensor_data['temperature']}°C")
        print(f"Humidity: {sensor_data['humidity']}%")
        print(f"Light Intensity: {sensor_data['light_intensity']} lux")
        print(f"Water Level: {sensor_data['water_level']}%")
        print(f"Pump Status: {pump_status}")

        if alerts:

            print("\nALERTS:")

            for alert in alerts:
                print(f"-> {alert}")

        print("===================================\n")

        time.sleep(5)

# ==============================
# START PROGRAM
# ==============================

if __name__ == "__main__":
    main()