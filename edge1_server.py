from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

EDGE_NODE_ID = "edge_1"
FOG_URL = "http://127.0.0.1:6001/process"

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
        print(f"[EDGE {EDGE_NODE_ID}] Received from {data.get('device_id','?')} | sensor_status: faulty | dropping (missing field)")
        return jsonify({"error": f"Missing field: {missing[0]}"}), 400

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

    data["sensor_status"] = "ok"
    data["edge_node_id"] = EDGE_NODE_ID
    data["edge_timestamp"] = datetime.utcnow().isoformat(timespec='seconds')
    
    try:
        resp = requests.post(FOG_URL, json=data, timeout=5)
        print(f"[EDGE {EDGE_NODE_ID}] Received from {data['device_id']} | sensor_status: ok | forwarding to fog")
    except Exception as e:
        print(f"[EDGE {EDGE_NODE_ID}] FORWARD ERROR: {e}")
        return jsonify({"error": "Fog unreachable"}), 502

    return jsonify({"status": "forwarded"}), 200

if __name__ == "__main__":
    print("[EDGE] Starting Edge Node 1 on port 5001...")
    app.run(host="127.0.0.1", port=5001)
