from flask import Flask, render_template, jsonify
from draw import doDraw, writeDraw
from flask_socketio import SocketIO, emit
import time
class MyClass:
    def __init__(self):
        self.winners = ["","",""]
        self.isRunning = 0

    def update_strings(self):
        socketio.emit('update', {'strings': self.winners})

app = Flask(__name__)
site_obj = MyClass()
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/start', methods=['POST'])
def buttonStart():
    #start
    site_obj.isRunning = 1
    return render_template('index.html', output=site_obj.winners)

@app.route('/stop', methods=['POST'])
def buttonStop():
    # Function to perform (in this case, do nothing)
    site_obj.isRunning = 0
    site_obj.update_strings()
    time.sleep(0.01)
    return render_template('index.html', output=site_obj.winners)

@app.route('/spam')
def spam():
    while site_obj.isRunning == 1:
        site_obj.winners = doDraw()
        site_obj.update_strings()
    site_obj.update_strings()
    return ""

@socketio.on('connect')
def handle_connect():

    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    

if __name__ == '__main__':
    socketio.run(app, debug="True")