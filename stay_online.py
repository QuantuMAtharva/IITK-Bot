from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hey! I am running fine"
def run():
    app.run(host='0.0.0.0', port=8080)
def stay_online():
    t = Thread(target=run)
    t.start()