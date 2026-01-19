# IoT-Health-Monitoring-System
Multi-node IoT health monitoring system using ESP8266, featuring real-time heart rate, SpO2 (MAX30102), and environmental data transmission with experimental signal processing.
# Multi-Node IoT Health Monitoring System

An end-to-end IoT solution for real-time health and environmental monitoring, designed and implemented using **ESP8266** nodes and a **Raspberry Pi** central hub.

## Overview
This project focuses on the integration of various medical and environmental sensors into a multi-node architecture. The system identifies and overcomes the real-world limitations of low-cost sensors through experimental signal processing logic.

## 🛠 Tech Stack & Tools
- **Microcontrollers:** ESP8266 (NodeMCU)
- **Central Hub:** Raspberry Pi
- **Communication:** HTTP / JSON
- **Protocols:** I2C, One-Wire, Serial (UART)
- **Programming:** C++ (Arduino IDE), Python (Data Handling)

## 📡 Sensor Integration
| Sensor | Function | Protocol |
| :--- | :--- | :--- |
| **MAX30102** | Heart Rate & SpO2 | I2C |
| **DS18B20** | Body Temperature | One-Wire |
| **DHT11** | Ambient Temp & Humidity | Single-Bus (Custom) |

## 🧠 Key Challenges & Solutions
- **Signal Integrity:** Theoretical filters were insufficient for the MAX30102 sensor noise. I developed **experimentally adapted signal processing logic**, including DC removal and adaptive peak detection, to achieve stable readings.
- **Reliability:** Implemented a robust **HTTP/JSON communication layer** with automatic reconnection handling to ensure continuous data flow to the central hub.
- **Accuracy:** Validated results against reference medical devices, achieving an accuracy of **±10 bpm** for heart rate and **±3%** for SpO2.

## 📈 System Architecture
1. **Node Level:** Each ESP8266 node collects data from sensors and applies initial filtering.
2. **Transmission:** Data is encapsulated in JSON format and sent via HTTP POST requests.
3. **Hub Level:** Raspberry Pi receives and logs data for further analysis or visualization.

---
*Developed by Emir Gülsoy as part of the Undergraduate Graduation Project at Istanbul Technical University (ITU).*
