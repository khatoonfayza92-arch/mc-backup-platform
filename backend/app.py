from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Multi-Cloud Backup Platform",
        "service": "Backup Orchestrator",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "service": "Multi-Cloud Backup Platform",
        "status": "healthy"
    })


@app.route("/api/backups")
def backups():
    return jsonify([
        {
            "backup_id": 1,
            "cloud": "AWS",
            "status": "Completed"
        },
        {
            "backup_id": 2,
            "cloud": "Azure",
            "status": "Completed"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    