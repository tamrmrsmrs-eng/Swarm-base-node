import os
import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({
        "status": "active",
        "node_id": os.environ.get('NODE_ID', 'unknown'),
        "version": "1.0.0"
    })

@app.route('/vfs/store', methods=['POST'])
def store():
    # Placeholder for DNA-VFS light
    return jsonify({"status": "stored", "id": "demo-id"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Swarm node starting on port {port}")
    app.run(host='0.0.0.0', port=port)
