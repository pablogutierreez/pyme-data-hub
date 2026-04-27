import os
from flask import Flask, jsonify
from main import run_multi_niche_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "pyme-data-hub"}), 200

@app.route("/run-pipeline", methods=["POST"])
def trigger_pipeline():
    """Endpoint for Cloud Scheduler to trigger the ETL pipeline."""
    try:
        run_multi_niche_pipeline()
        return jsonify({"status": "success", "message": "Pipeline executed successfully"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)