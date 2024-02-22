from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    pod_id = socket.gethostname()
    return f'Hello World! This is pod {pod_id}.\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
