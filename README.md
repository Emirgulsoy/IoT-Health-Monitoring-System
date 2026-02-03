# Multi-Node IoT Health Monitoring System

This repository contains an ESP8266-based multi-node IoT health monitoring system developed as an undergraduate graduation project.

The primary focus of the project is not only data acquisition, but handling real-world limitations of low-cost physiological sensors such as noise, instability, and unreliable library-level processing.

---

## Project Overview

- 5 independent ESP8266 (NodeMCU) sensor nodes
- Central Raspberry Pi hub for data collection
- HTTP/JSON-based communication architecture
- Emphasis on stability and repeatability rather than medical-grade precision

---

## Tech Stack & Tools

- **Microcontrollers:** ESP8266 (NodeMCU)
- **Central Hub:** Raspberry Pi
- **Communication:** HTTP / JSON
- **Protocols:** I2C, One-Wire, UART
- **Programming:** C++ (Arduino), Python (basic data handling)

---

## Sensor Integration

| Sensor | Purpose | Protocol |
|------|--------|---------|
| MAX30102 | Heart Rate & SpO₂ | I2C |
| DS18B20 | Body Temperature | One-Wire |
| DHT11 | Ambient Temperature & Humidity | Single-Bus |

---

## Key Challenges and Engineering Decisions

### Signal Noise and Sensor Limitations
Initial attempts using standard libraries and theoretical filtering techniques were insufficient due to sensor noise, motion artifacts, and hardware quality limitations.

To address this, I adopted an experimental and data-driven approach:
- DC offset removal to isolate pulsatile components
- Adaptive peak detection instead of fixed thresholds
- Practical digital filtering tuned through repeated observation of raw signals

The signal processing logic was refined iteratively rather than relying solely on textbook models.

### Communication Reliability
Implemented an HTTP/JSON-based communication layer with automatic reconnection handling to maintain data flow under unstable Wi-Fi conditions.

---

## System Architecture

1. **Node Level:** ESP8266 nodes acquire sensor data and apply initial signal conditioning.
2. **Transmission:** Processed data is encapsulated in JSON and sent via HTTP POST.
3. **Hub Level:** Raspberry Pi receives and logs data for monitoring and validation.

---

## Results

- Heart Rate accuracy: approximately ±10 bpm
- SpO₂ accuracy: approximately ±3%
- Results validated through comparison with reference consumer devices

---

## Limitations and Future Improvements

- Polling-based sampling was used; timer/interrupt-based sampling could improve timing stability
- Sensor quality limits achievable accuracy
- Future improvements may include synchronized sampling and improved hardware

---

## Project Ownership

This project was fully designed, implemented, debugged, and validated independently as part of an undergraduate graduation project at Istanbul Technical University (ITU).

## Project Context
This project was developed as an undergraduate graduation by Emir Gülsoy at Istanbul Technical University (ITU).
The focus was not only implementation but also understanding real-world limitations of low-cost sensors.

