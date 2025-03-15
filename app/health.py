from flask import jsonify
from app import app  # Import the Flask app instance

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        "request_count": 100,
        "memory_usage": "50MB"
    }), 200
