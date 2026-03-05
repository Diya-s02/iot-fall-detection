from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def detect_fall(data):
    if abs(data["accel_x"]) > 15:
        return True, f"accel_x > 15 (value: {data['accel_x']})"
    if abs(data["accel_y"]) > 15:
        return True, f"accel_y > 15 (value: {data['accel_y']})"
    if data["accel_z"] < 3.0:
        return True, f"accel_z < 3.0 (value: {data['accel_z']})"
    if abs(data["gyro_x"]) > 10:
        return True, f"gyro_x > 10 (value: {data['gyro_x']})"
    if abs(data["gyro_y"]) > 10:
        return True, f"gyro_y > 10 (value: {data['gyro_y']})"
    if abs(data["gyro_z"]) > 10:
        return True, f"gyro_z > 10 (value: {data['gyro_z']})"
    if data["heart_rate"] < 45:
        return True, f"heart_rate < 45 (value: {data['heart_rate']})"
    if data["heart_rate"] > 130:
        return True, f"heart_rate > 130 (value: {data['heart_rate']})"
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
        print(f"\n[ALERT] FALL DETECTED")
        print(f"  Patient  : {data['patient_id']}")
        print(f"  Device   : {data['device_id']}")
        print(f"  Edge Node: {data.get('edge_node_id','?')}")
        print(f"  Timestamp: {data.get('edge_timestamp', '?')}")
        print(f"  Trigger  : {trigger}")
        print(f"  Heart Rate: {data['heart_rate']} bpm")
        print(f"  Location : ({data['gps_lat']}, {data['gps_lon']})\n")
        return jsonify({"status":"processed", "alert": True}), 200
    else:
        print(f"[FOG] Normal - {data['patient_id']} | HR: {data['heart_rate']} | accel_z: {data['accel_z']} | edge: {data.get('edge_node_id','?')}")
        return jsonify({"status":"processed", "alert": False}), 200

if __name__ == "__main__":
    print("[FOG] Starting Fog Node on port 6001...")
    app.run(host="127.0.0.1", port=6001)