from flask import Flask
app = Flask(__name__)
import asyncio
import websockets

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    socketio.run(app)
