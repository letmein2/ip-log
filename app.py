from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
LOG_DIR = "login_logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.route('/api/loglogin', methods=['POST'])
def log_login():
    data = request.get_json()
    username = data.get('username')
    computer = data.get('computerName')
    ip = data.get('publicIP')
    timestamp = data.get('timestamp', datetime.utcnow().isoformat())
    log_entry = f"{timestamp} - User: {username} - Computer: {computer} - Public IP: {ip}\n"
    log_file = os.path.join(LOG_DIR, f"{datetime.utcnow().date()}.log")
    with open(log_file, "a") as f:
        f.write(log_entry)
    return jsonify({"status": "success"}), 200
