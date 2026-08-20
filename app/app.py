from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "application": "Azure Production Web Platform",
        "environment": os.getenv("ENVIRONMENT", "local"),
        "version": os.getenv("APP_VERSION", "v1"),
        "status": "healthy"
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


@app.route("/ready")
def ready():
    return {
        "status": "ready"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
