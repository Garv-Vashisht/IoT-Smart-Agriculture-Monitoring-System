# 🌱 IoT-Enabled Smart Agriculture Monitoring System

An industry-oriented IoT project that monitors agricultural field conditions in real time using sensors, automation logic, dashboards, data analytics, and embedded systems integration.

This project simulates a smart farming environment where soil moisture, temperature, humidity, light intensity, and water level are continuously monitored to automate irrigation decisions and generate alerts.

---

# 📌 Problem Statement

Traditional farming methods depend heavily on manual monitoring and irrigation, which can result in:

- Water wastage
- Poor crop productivity
- Delayed irrigation
- Increased labor costs
- Lack of real-time monitoring
- Inefficient farm management

This project solves these issues using IoT-based smart automation and real-time monitoring.

---

# 🎯 Project Objectives

- Monitor environmental conditions in real time
- Automate irrigation logic
- Generate alerts for abnormal conditions
- Log historical sensor data
- Visualize analytics through dashboard
- Demonstrate IoT and embedded systems concepts
- Create an industry-level GitHub portfolio project

---

# 🚀 Features

## ✅ Real-Time Monitoring
- Soil Moisture
- Temperature
- Humidity
- Light Intensity
- Water Level

## ✅ Smart Irrigation System
- Automatic Pump ON/OFF logic
- Threshold-based automation

## ✅ Alerts & Notifications
- Low Soil Moisture Alert
- High Temperature Alert
- Low Water Level Alert

## ✅ Dashboard Visualization
- Streamlit dashboard
- Live charts
- Historical trends

## ✅ Data Logging
- CSV logging
- Alert logs
- System reports

## ✅ Embedded Systems Support
- ESP32 integration
- Arduino firmware
- MQTT-ready structure

## ✅ Analytics
- Temperature trends
- Soil moisture analytics
- Humidity analysis
- Pump usage statistics

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Simulation & automation |
| ESP32 | IoT controller |
| Arduino IDE | Embedded programming |
| Streamlit | Dashboard |
| Pandas | Data analysis |
| Matplotlib | Chart generation |
| MQTT | IoT communication |
| GitHub | Version control |
| Wokwi | IoT simulation |

---

# 🏗️ System Architecture

```text
Sensors
   ↓
ESP32 / Python Simulation
   ↓
Data Collection
   ↓
Threshold Analysis
   ↓
Automation Logic
   ↓
Alert Generation
   ↓
Dashboard Visualization
   ↓
Pump Control
   ↓
CSV Logging & Reports
```

---

# ⚙️ Components Used

## Hardware Components

| Component | Purpose |
|---|---|
| ESP32 | IoT microcontroller |
| DHT11/DHT22 | Temperature & humidity |
| Soil Moisture Sensor | Soil monitoring |
| LDR Sensor | Light intensity |
| Water Level Sensor | Tank monitoring |
| Relay Module | Pump control |
| Water Pump | Irrigation simulation |

---

# 🔌 Wiring Overview

| Component | ESP32 Pin |
|---|---|
| DHT11 Data | GPIO 4 |
| Soil Moisture | GPIO 34 |
| LDR Sensor | GPIO 35 |
| Relay Module | GPIO 25 |

---

# 📂 Project Structure

```text
IoT-Smart-Agriculture-Monitoring-System/
│
├── arduino_code/
│   │
│   ├── smart_agriculture/
│   │   └── smart_agriculture.ino
│   │
│   ├── esp32_mqtt_code/
│   │   └── esp32_mqtt_code.ino
│   │
│   ├── sensor_test_code/
│   │   └── sensor_test_code.ino
│   │
│   ├── relay_test/
│   │   └── relay_test.ino
│   │
│   └── README.md
│
├── dashboard/
│   └── dashboard.py
│
├── python_simulation/
│
├── data/
│   └── sensor_data.csv
│
├── outputs/
│   └── alerts.txt
│
├── images/
│   ├── temperature_chart.png
│   ├── humidity_chart.png
│   └── soil_moisture_chart.png
│
├── docs/
│   └── system_report.txt
│
├── circuit_diagram/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

# 🔥 Workflow

```text
Sensor Data Collection
        ↓
Data Processing
        ↓
Threshold Checking
        ↓
Alert Generation
        ↓
Pump Control Logic
        ↓
Dashboard Visualization
        ↓
CSV Logging & Analytics
```

---

# 💻 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/IoT-Smart-Agriculture-Monitoring-System.git
```

---

## 2️⃣ Open Project

Open project in VS Code.

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Python Simulation

```bash
python main.py
```

Expected Output:

```text
SMART AGRICULTURE MONITORING SYSTEM STARTED

Soil Moisture: 25%
Temperature: 39°C
Humidity: 70%
Pump Status: ON

ALERTS:
-> Low Soil Moisture Detected
-> High Temperature Alert
```

---

# 📊 Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

Dashboard Features:
- Live sensor readings
- Temperature charts
- Humidity trends
- Soil moisture analytics

---

# 📈 Generated Outputs

## 📁 data/
- sensor_data.csv

## 📁 outputs/
- alerts.txt

## 📁 docs/
- system_report.txt

## 📁 images/
- temperature_chart.png
- humidity_chart.png
- soil_moisture_chart.png

---

# 🌐 IoT Dashboard Integration

This project supports:
- ThingSpeak
- Node-RED
- MQTT Broker
- Blynk
- Grafana

---

# 🧪 Simulation Platforms

- Wokwi
- Tinkercad
- Python Simulation

---

# 📷 Screenshots To Add

## Recommended Screenshots
- VS Code project structure
- Streamlit dashboard
- CSV data logs
- Charts & analytics
- Wokwi simulation
- Serial monitor output
- GitHub repository preview

---

# 📊 Threshold Conditions

| Condition | Action |
|---|---|
| Soil Moisture < 40% | Pump ON |
| Temperature > 35°C | High Temp Alert |
| Water Level < 20% | Water Alert |

---

# 🛠️ Arduino Modules

## smart_agriculture
Main irrigation automation logic.

## esp32_mqtt_code
MQTT cloud communication.

## sensor_test_code
Sensor calibration/testing.

## relay_test
Pump relay testing.

---

# ☁️ MQTT Integration

The project architecture supports MQTT communication using:
- ESP32 WiFi
- MQTT Broker
- Cloud dashboards
- Real-time publishing

Example MQTT topic:

```text
farm/status
```

---

# 📚 Learning Outcomes

Through this project, I learned:

- IoT architecture
- Embedded systems
- Sensor integration
- Automation logic
- Dashboard development
- Data visualization
- MQTT communication
- GitHub project management
- Python analytics

---

# 🌍 Real-World Applications

- Smart irrigation systems
- Precision farming
- Greenhouse automation
- Agricultural analytics
- Water management systems
- Smart farming startups

---

# 🏭 Industry Relevance

Similar technologies are used by:
- John Deere
- Bosch AgriTech
- CropX
- AWS IoT Agriculture
- Azure FarmBeats

---

# 📈 Future Improvements

- Weather API integration
- AI crop prediction
- Solar-powered node
- LoRa communication
- Mobile notifications
- TinyML integration
- Cloud deployment
- Fertilizer automation

---

# 🧠 Interview Questions

## 1. Explain your project.

This project is an IoT-based Smart Agriculture Monitoring System that monitors soil moisture, temperature, humidity, light intensity, and water level using sensors. Based on threshold conditions, the system automates irrigation decisions and generates alerts. The project includes Python simulation, Streamlit dashboard visualization, CSV logging, analytics, and ESP32 integration for real-time smart farming applications.

---

## 2. What problem does this solve?

It reduces water wastage and manual monitoring by automating irrigation and environmental monitoring.

---

## 3. Which sensors are used?

- DHT11/DHT22
- Soil Moisture Sensor
- LDR Sensor
- Water Level Sensor

---

## 4. Why use ESP32?

ESP32 provides built-in WiFi support for IoT communication and cloud integration.

---

## 5. How does pump automation work?

If soil moisture falls below threshold value, the pump automatically turns ON.

---

## 6. Why is data logging important?

It helps analyze historical trends and optimize irrigation patterns.

---

## 7. Which dashboard technology is used?

Streamlit dashboard for real-time visualization.

---

## 8. How can this project be improved?

Adding AI prediction, weather APIs, mobile apps, and cloud deployment.

---

## 9. Which communication protocol is used?

MQTT protocol for lightweight IoT communication.

---

## 10. What are the key learning outcomes?

IoT systems, automation, embedded programming, analytics, and dashboard development.

---

# 📌 GitHub Topics

```text
iot
smart-agriculture
python
esp32
arduino
streamlit
dashboard
automation
embedded-systems
mqtt
data-analytics
```

---

# 👨‍💻 Author

Garv Vashisht

---

# ⭐ Support

If you found this project useful, give this repository a star ⭐