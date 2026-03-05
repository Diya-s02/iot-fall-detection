# IoT Fall Detection System (Simulated)

## Overview

A 3-tier simulated IoT system for real-time patient fall detection.

- IoT Layer: 4 device simulators send data every 2 seconds
- Edge Layer: 2 Flask edge nodes validate and preprocess
- Fog Layer: 1 Flask fog node detects falls and logs alerts

## Quick Start

1. Install requirements: pip install requests
2. Start Docker: docker-compose up --build
3. Run devices (4 terminals): python iot/device1.py, python iot/device2.py, etc.
4. Monitor: docker logs fog -f

## Fall Detection

Triggered when any of these conditions are met:
- Acceleration spike: |accel_x| > 15 OR |accel_y| > 15 OR accel_z < 3.0
- Gyroscope spike: |gyro_x| > 10 OR |gyro_y| > 10 OR |gyro_z| > 10
- Heart rate anomaly: heart_rate < 45 OR heart_rate > 130
- Event flag: event == "fall_detected"
