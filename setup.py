import os

# File structure definition
files = {
    'iot/device1.py': '''import requests
import time
import random
from datetime import datetime

DEVICE_CONFIG = {
    "device_id": "device_1",
    "patient_id": "patient_1",
    "EDGE_URL": "http://localhost:5001/ingest"
}

def generate_payload():
    is_fall = random.random() < 0.10
    now_iso = datetime.utcnow().isoformat(timespec='seconds')

    def rand_norm(low, high):
        return round(random.uniform(low, high), 2)
    
    def rand_anom(low, high):
        return round(random.uniform(low, high) * random.choice([-1, 1]), 2)

    if is_fall:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_anom(15.1, 20.0),
            "accel_y": rand_anom(15.1, 20.0),
            "accel_z": round(random.uniform(0.0, 2.9), 2),
            "gyro_x": rand_anom(10.1, 15.0),
            "gyro_y": rand_anom(10.1, 15.0),
            "gyro_z": rand_anom(10.1, 15.0),
            "heart_rate": random.choice([random.randint(30, 39), random.randint(141, 160)]),
            "gps_lat": rand_norm(13.0827, 13.0830),
            "gps_lon": rand_norm(80.2707, 80.2710),
            "event": "fall_detected"
        }
    else:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_norm(-2.0, 2.0),
            "accel_y": rand_norm(-2.0, 2.0),
            "accel_z": rand_norm(8.5, 10.5),
            "gyro_x": rand_norm(-1.0, 1.0),
            "gyro_y": rand_norm(-1.0, 1.0),
            "gyro_z": rand_norm(-1.0, 1.0),
            "heart_rate": int(rand_norm(55, 100)),
            "gps_lat": rand_norm(13.0827, 13.0830),
            "gps_lon": rand_norm(80.2707, 80.2710),
            "event": "normal"
        }
    return payload

def main():
    while True:
        payload = generate_payload()
        print("[{}] Sending: {}".format(
            DEVICE_CONFIG["device_id"], payload))
        try:
            resp = requests.post(DEVICE_CONFIG["EDGE_URL"], json=payload)
            print("[{}] Edge response: {} {}".format(
                DEVICE_CONFIG["device_id"], resp.status_code, resp.text.strip()))
        except Exception as e:
            print("[{}] POST error: {}".format(
                DEVICE_CONFIG["device_id"], e))
        time.sleep(2)

if __name__ == "__main__":
    main()
''',

    'iot/device2.py': '''import requests
import time
import random
from datetime import datetime

DEVICE_CONFIG = {
    "device_id": "device_2",
    "patient_id": "patient_2",
    "EDGE_URL": "http://localhost:5001/ingest"
}

def generate_payload():
    is_fall = random.random() < 0.10
    now_iso = datetime.utcnow().isoformat(timespec='seconds')

    def rand_norm(low, high):
        return round(random.uniform(low, high), 2)
    
    def rand_anom(low, high):
        return round(random.uniform(low, high) * random.choice([-1, 1]), 2)

    if is_fall:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_anom(15.1, 20.0),
            "accel_y": rand_anom(15.1, 20.0),
            "accel_z": round(random.uniform(0.0, 2.9), 2),
            "gyro_x": rand_anom(10.1, 15.0),
            "gyro_y": rand_anom(10.1, 15.0),
            "gyro_z": rand_anom(10.1, 15.0),
            "heart_rate": random.choice([random.randint(30, 39), random.randint(141, 160)]),
            "gps_lat": rand_norm(13.0810, 13.0813),
            "gps_lon": rand_norm(80.2750, 80.2753),
            "event": "fall_detected"
        }
    else:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_norm(-2.0, 2.0),
            "accel_y": rand_norm(-2.0, 2.0),
            "accel_z": rand_norm(8.5, 10.5),
            "gyro_x": rand_norm(-1.0, 1.0),
            "gyro_y": rand_norm(-1.0, 1.0),
            "gyro_z": rand_norm(-1.0, 1.0),
            "heart_rate": int(rand_norm(55, 100)),
            "gps_lat": rand_norm(13.0810, 13.0813),
            "gps_lon": rand_norm(80.2750, 80.2753),
            "event": "normal"
        }
    return payload

def main():
    while True:
        payload = generate_payload()
        print("[{}] Sending: {}".format(
            DEVICE_CONFIG["device_id"], payload))
        try:
            resp = requests.post(DEVICE_CONFIG["EDGE_URL"], json=payload)
            print("[{}] Edge response: {} {}".format(
                DEVICE_CONFIG["device_id"], resp.status_code, resp.text.strip()))
        except Exception as e:
            print("[{}] POST error: {}".format(
                DEVICE_CONFIG["device_id"], e))
        time.sleep(2)

if __name__ == "__main__":
    main()
''',

    'iot/device3.py': '''import requests
import time
import random
from datetime import datetime

DEVICE_CONFIG = {
    "device_id": "device_3",
    "patient_id": "patient_3",
    "EDGE_URL": "http://localhost:5002/ingest"
}

def generate_payload():
    is_fall = random.random() < 0.10
    now_iso = datetime.utcnow().isoformat(timespec='seconds')

    def rand_norm(low, high):
        return round(random.uniform(low, high), 2)
    
    def rand_anom(low, high):
        return round(random.uniform(low, high) * random.choice([-1, 1]), 2)

    if is_fall:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_anom(15.1, 20.0),
            "accel_y": rand_anom(15.1, 20.0),
            "accel_z": round(random.uniform(0.0, 2.9), 2),
            "gyro_x": rand_anom(10.1, 15.0),
            "gyro_y": rand_anom(10.1, 15.0),
            "gyro_z": rand_anom(10.1, 15.0),
            "heart_rate": random.choice([random.randint(30, 39), random.randint(141, 160)]),
            "gps_lat": rand_norm(13.0800, 13.0803),
            "gps_lon": rand_norm(80.2710, 80.2713),
            "event": "fall_detected"
        }
    else:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_norm(-2.0, 2.0),
            "accel_y": rand_norm(-2.0, 2.0),
            "accel_z": rand_norm(8.5, 10.5),
            "gyro_x": rand_norm(-1.0, 1.0),
            "gyro_y": rand_norm(-1.0, 1.0),
            "gyro_z": rand_norm(-1.0, 1.0),
            "heart_rate": int(rand_norm(55, 100)),
            "gps_lat": rand_norm(13.0800, 13.0803),
            "gps_lon": rand_norm(80.2710, 80.2713),
            "event": "normal"
        }
    return payload

def main():
    while True:
        payload = generate_payload()
        print("[{}] Sending: {}".format(
            DEVICE_CONFIG["device_id"], payload))
        try:
            resp = requests.post(DEVICE_CONFIG["EDGE_URL"], json=payload)
            print("[{}] Edge response: {} {}".format(
                DEVICE_CONFIG["device_id"], resp.status_code, resp.text.strip()))
        except Exception as e:
            print("[{}] POST error: {}".format(
                DEVICE_CONFIG["device_id"], e))
        time.sleep(2)

if __name__ == "__main__":
    main()
''',

    'iot/device4.py': '''import requests
import time
import random
from datetime import datetime

DEVICE_CONFIG = {
    "device_id": "device_4",
    "patient_id": "patient_4",
    "EDGE_URL": "http://localhost:5002/ingest"
}

def generate_payload():
    is_fall = random.random() < 0.10
    now_iso = datetime.utcnow().isoformat(timespec='seconds')

    def rand_norm(low, high):
        return round(random.uniform(low, high), 2)
    
    def rand_anom(low, high):
        return round(random.uniform(low, high) * random.choice([-1, 1]), 2)

    if is_fall:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_anom(15.1, 20.0),
            "accel_y": rand_anom(15.1, 20.0),
            "accel_z": round(random.uniform(0.0, 2.9), 2),
            "gyro_x": rand_anom(10.1, 15.0),
            "gyro_y": rand_anom(10.1, 15.0),
            "gyro_z": rand_anom(10.1, 15.0),
            "heart_rate": random.choice([random.randint(30, 39), random.randint(141, 160)]),
            "gps_lat": rand_norm(13.0860, 13.0863),
            "gps_lon": rand_norm(80.2740, 80.2743),
            "event": "fall_detected"
        }
    else:
        payload = {
            "device_id": DEVICE_CONFIG["device_id"],
            "patient_id": DEVICE_CONFIG["patient_id"],
            "timestamp": now_iso,
            "accel_x": rand_norm(-2.0, 2.0),
            "accel_y": rand_norm(-2.0, 2.0),
            "accel_z": rand_norm(8.5, 10.5),
            "gyro_x": rand_norm(-1.0, 1.0),
            "gyro_y": rand_norm(-1.0, 1.0),
            "gyro_z": rand_norm(-1.0, 1.0),
            "heart_rate": int(rand_norm(55, 100)),
            "gps_lat": rand_norm(13.0860, 13.0863),
            "gps_lon": rand_norm(80.2740, 80.2743),
            "event": "normal"
        }
    return payload

def main():
    while True:
        payload = generate_payload()
        print("[{}] Sending: {}".format(
            DEVICE_CONFIG["device_id"], payload))
        try:
            resp = requests.post(DEVICE_CONFIG["EDGE_URL"], json=payload)
            print("[{}] Edge response: {} {}".format(
                DEVICE_CONFIG["device_id"], resp.status_code, resp.text.strip()))
        except Exception as e:
            print("[{}] POST error: {}".format(
                DEVICE_CONFIG["device_id"], e))
        time.sleep(2)

if __name__ == "__main__":
    main()
''',

    'edge/requirements.txt': '''flask==3.0.0
requests==2.31.0
''',

    'edge/edge_node.py': '''import os
from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

EDGE_NODE_ID = os.environ.get("EDGE_NODE_ID", "edge_x")
FOG_HOST = os.environ.get("FOG_HOST", "http://fog:6001")
PORT = int(os.environ.get("PORT", "5001"))

REQUIRED_FIELDS = [
    "device_id", "patient_id", "timestamp",
    "accel_x", "accel_y", "accel_z",
    "gyro_x", "gyro_y", "gyro_z",
    "heart_rate", "gps_lat", "gps_lon", "event"
]

SENSOR_BOUNDS = {
    "accel_x": (-50.0, 50.0),
    "accel_y": (-50.0, 50.0),
    "accel_z": (-50.0, 50.0),
    "gyro_x": (-30.0, 30.0),
    "gyro_y": (-30.0, 30.0),
    "gyro_z": (-30.0, 30.0),
    "heart_rate": (20, 250)
}

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON"}), 400
    
    missing = [f for f in REQUIRED_FIELDS if f not in data]
    if missing:
        resp = {"error": f"Missing field: {missing[0]}"}
        print(f"[EDGE {EDGE_NODE_ID}] Received from {data.get('device_id','?')} | sensor_status: faulty | dropping (missing {missing[0]})")
        return jsonify(resp), 400

    # Check range
    faulty = False
    reason = ""
    for k, (lo, hi) in SENSOR_BOUNDS.items():
        v = data[k]
        if not (lo <= v <= hi):
            faulty = True
            reason = f"{k} out of range"
            break

    if faulty:
        print(f"[EDGE {EDGE_NODE_ID}] Received from {data['device_id']} | sensor_status: faulty | dropping ({reason})")
        return jsonify({"error": reason}), 422

    # Preprocess: add sensor_status, edge_node_id, edge_timestamp
    data["sensor_status"] = "ok"
    data["edge_node_id"] = EDGE_NODE_ID
    data["edge_timestamp"] = datetime.utcnow().isoformat(timespec='seconds')
    
    # Forward to fog
    try:
        fog_url = FOG_HOST.rstrip("/") + "/process"
        resp = requests.post(fog_url, json=data, timeout=5)
        print(f"[EDGE {EDGE_NODE_ID}] Received from {data['device_id']} | sensor_status: ok | forwarding to fog")
    except Exception as e:
        print(f"[EDGE {EDGE_NODE_ID}] FORWARD ERROR: {e}")
        return jsonify({"error": "Fog unreachable"}), 502

    return jsonify({"status": "forwarded"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
''',

    'edge/Dockerfile': '''FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY edge_node.py .
CMD ["python", "edge_node.py"]
''',

    'fog/requirements.txt': '''flask==3.0.0
requests==2.31.0
''',

    'fog/fog_node.py': '''import os
from flask import Flask, request, jsonify

app = Flask(__name__)
PORT = int(os.environ.get("PORT", "6001"))

def detect_fall(data):
    # 1. Acceleration spike
    if abs(data["accel_x"]) > 15:
        return True, f"accel_x > 15 (value: {data['accel_x']})"
    if abs(data["accel_y"]) > 15:
        return True, f"accel_y > 15 (value: {data['accel_y']})"
    if data["accel_z"] < 3.0:
        return True, f"accel_z < 3.0 (value: {data['accel_z']})"
    # 2. Gyro spike
    if abs(data["gyro_x"]) > 10:
        return True, f"gyro_x > 10 (value: {data['gyro_x']})"
    if abs(data["gyro_y"]) > 10:
        return True, f"gyro_y > 10 (value: {data['gyro_y']})"
    if abs(data["gyro_z"]) > 10:
        return True, f"gyro_z > 10 (value: {data['gyro_z']})"
    # 3. Heart rate anomaly
    if data["heart_rate"] < 45:
        return True, f"heart_rate < 45 (value: {data['heart_rate']})"
    if data["heart_rate"] > 130:
        return True, f"heart_rate > 130 (value: {data['heart_rate']})"
    # 4. Event flag
    if data["event"] == "fall_detected":
        return True, f"event == fall_detected"
    return False, ""

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON"}), 400
    
    fall, trigger = detect_fall(data)
    if fall:
        print(f"""[ALERT] 🚨 FALL DETECTED
  Patient  : {data['patient_id']}
  Device   : {data['device_id']}
  Edge Node: {data.get('edge_node_id','?')}
  Timestamp: {data.get('edge_timestamp', '?')}
  Trigger  : {trigger}
  Heart Rate: {data['heart_rate']} bpm
  Location : ({data['gps_lat']}, {data['gps_lon']})
""")
        return jsonify({"status":"processed", "alert": True}), 200
    else:
        print(f"[FOG] ✅ Normal — {data['patient_id']} | HR: {data['heart_rate']} | accel_z: {data['accel_z']} | edge: {data.get('edge_node_id','?')}")
        return jsonify({"status":"processed", "alert": False}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
''',

    'fog/Dockerfile': '''FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY fog_node.py .
CMD ["python", "fog_node.py"]
''',

    'docker-compose.yml': '''version: "3.9"

services:

  fog:
    build: ./fog
    container_name: fog
    ports:
      - "6001:6001"
    environment:
      - PORT=6001
    networks:
      - iot_net

  edge1:
    build: ./edge
    container_name: edge1
    ports:
      - "5001:5001"
    environment:
      - EDGE_NODE_ID=edge_1
      - FOG_HOST=http://fog:6001
      - PORT=5001
    depends_on:
      - fog
    networks:
      - iot_net

  edge2:
    build: ./edge
    container_name: edge2
    ports:
      - "5002:5002"
    environment:
      - EDGE_NODE_ID=edge_2
      - FOG_HOST=http://fog:6001
      - PORT=5002
    depends_on:
      - fog
    networks:
      - iot_net

networks:
  iot_net:
    driver: bridge
''',

    'README.md': '''# IoT Fall Detection System

This is the complete implementation of an IoT Fall Detection system with Docker containers and Python simulators.

See README.md for full instructions.
'''
}

# Create directories
for file_path in files.keys():
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
        print(f"✅ Created directory: {directory}")

# Write all files
for file_path, content in files.items():
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✅ Created file: {file_path}")

print("\n✅✅✅ All files created successfully!")
print("\nNext steps:")
print("1. pip install requests")
print("2. docker-compose up --build")
print("3. python iot/device1.py (in separate terminals)")
