# app/main.py
from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Rota / acessada")
    return "Hello, Datadog!"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(host="0.0.0.0", port=5000)
