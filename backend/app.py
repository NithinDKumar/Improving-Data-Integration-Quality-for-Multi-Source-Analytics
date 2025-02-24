from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Allows React frontend to access Flask API

# Existing metrics endpoint
@app.route('/metrics')
def get_metrics():
    data = {
        "integration_accuracy": 95,
        "duplicate_rate": 5,
        "missing_values": 2
    }
    return jsonify(data)

# Conflict Resolution Logs API
@app.route('/conflicts')
def get_conflicts():
    conflict_logs = [
        {"id": 1, "field": "Name", "issue": "Duplicate entry", "resolved": False},
        {"id": 2, "field": "Date", "issue": "Incorrect format", "resolved": True},
    ]
    return jsonify(conflict_logs)

# File Upload API
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    df = pd.read_csv(file)

    # Basic data analysis
    response = {
        "columns": list(df.columns),
        "rows": len(df),
        "missing_values": df.isnull().sum().to_dict()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
