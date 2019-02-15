from flask import Flask
import json


app = Flask(__name__)


@app.route("/")
def home():
    return "Superup_DevOps-Challenge-Igal"

@app.route("/message")
def message():
    return "My message"

@app.route("/status")
def status():
    status_response = {"status": "completed", "container": "flatigal/devops-challenge-igal:tagname", "project": "https://github.com/flatigal70/devops-challenge-igal.git"}
    return json.dumps(status_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
