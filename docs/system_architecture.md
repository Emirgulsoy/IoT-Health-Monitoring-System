# System Architecture

The system consists of multiple ESP8266-based sensor nodes and a Raspberry Pi central hub.

## Node Layer
- ESP8266 (NodeMCU)
- Sensors: MAX30102, DS18B20, DHT11
- Local signal conditioning and filtering
- JSON-based HTTP POST transmission

## Communication Layer
- Wi-Fi
- HTTP / REST
- JSON payload structure

## Hub Layer
- Raspberry Pi
- Python-based data receiver
- Threshold-based alert logic
