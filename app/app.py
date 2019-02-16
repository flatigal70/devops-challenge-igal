from flask import Flask
import json,os
from crypt import AESCipher


app = Flask(__name__)


@app.route("/")
def home():
    return "Superup_DevOps-Challenge-Igal"

@app.route("/message")
def message():
    key = os.environ['key']
    cipher = AESCipher(key)
    encrypted = os.environ['encrypted']
    decrypted = cipher.decrypt(encrypted)
    return decrypted

@app.route("/status")
def status():
    status_response = {"status": "completed", "container": "flatigal/devops-challenge-igal:latest", "project": "https://github.com/flatigal70/devops-challenge-igal.git"}
    return json.dumps(status_response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
