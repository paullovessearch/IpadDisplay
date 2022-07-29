"""
Paul's Game Show Application

For managing the scores and screens for a game show.

Jul7 20, 2018

===================

Updated July 28, 2018

+ First Draft

"""

# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from functools import reduce

#import winsound
import json
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from threading import Thread, Event
import os
import sys

print("Python Version: " + sys.version)

#
# Initialize Flask & Socket IO for push notifications to clients
#

# sys.stdout = sys.stderr = open('ipad_log.out','wt',buffering=1)

__author__ = 'pnelson'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, logger=True, engineio_logger=True)

do_sound = False
sound_id = "ding"
starter_image = "/static/images/black.jpg"
active_image = "/static/imag-images/IMAG"


@app.after_request
def add_header(r):
    # r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


#
# Run Sounds as a background thread, so they will be delayed after the associated emit()'s
#

# class SoundThread(Thread):
    # def __init__(self, this_soundfile):
        # self.soundfile = this_soundfile
        # super(SoundThread, self).__init__()

    # def playsound(self):
        # print("PLAYING")
        # #winsound.PlaySound(self.soundfile, winsound.SND_FILENAME)
        # print("DONE-PLAYING")

    # def run(self):
        # self.playsound()

##
## MAIN INITIALIZATION
##

# Initialize Configuration


with open("config.json", "r", encoding="utf-8") as f:
  config = json.load(f)
print(json.dumps(config))

slides = config['slides']

button_event_id = 0


##
## HTTP Server ENDPOINTS
##

@app.route('/')
def index():
    print("Requesting Index File")
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


@app.route('/test')
def test_browser():
    return render_template('test.html')

@app.route('/reset')
def reset_game():
    pass
    return "ok"

@app.route('/button-press/<button_id>')
def button_press(button_id):
    global button_event_id
    socketio.emit('new-image', {'id': 42, 'image':active_image})
    return "ok"


@app.route('/status')
def status_console():
#    global scores, selects
#    print("Initiate Status Console")
#    return render_template( 'status-console.html', scores=scores, selects=list(map(lambda x: str(x).lower(), selects)) )
    pass
    return "ok"

@app.route('/view/<view_id>')
def view_page(view_id):
    print("View Image Console")
    return render_template('view-image.html', view_id=view_id, view_image=starter_image)


@socketio.on('connect')
def statmsg_connect():
    print('Client connected')


@socketio.on('disconnect')
def statmsg_disconnect():
    print('Client disconnected')


@socketio.on('new-device')
def handle_new_device(msg):
    print('New Device: ' + str(msg))

##
## MAIN
##

# set_curslide(0)
# print(cur_slideurl)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=80)
    #socketio.run(app)

