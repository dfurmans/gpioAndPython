import sys;
import RPi.GPIO as GPIO
import time
import threading
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, disconnect

if sys.version_info[0]>2: #Just making sure the program works with both Python 2.x and 3.x
    from queue import Queue
else:
    from Queue import Queue
app = Flask(__name__)
app.debug = False
socketio = SocketIO(app)

#REST
@app.route("/")
def hello():
    return render_template('index.html')
GPIO.setmode(GPIO.BOARD) # sprawdz co znaczy BCM

class Przycisk:
    def __init__(self, pin, trybGPIO, nazwaSedziego, colorPrzycisku, glosNaTak):
        self.config = GPIO.setup(pin, trybGPIO, pull_up_down=GPIO.PUD_UP)
        self.pin = pin
        self.tryp = trybGPIO
        self.nazwaSedziego = nazwaSedziego
        self.color = colorPrzycisku
        self.glosNaTak = glosNaTak
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.odbierzZmianeStanu, bouncetime=800)
        

    def odbierzZmianeStanu(self, channel):
        print("Pin:: "+ str(self.pin) + " Sedzia:: " + self.nazwaSedziego + " kolor:: " + self.color + " czyGlosZa " + str(self.glosNaTak))
        time.sleep(50.0 / 1000.0)
        socketio.emit('message', {
                                 'data': 'DaneZSocketIO', "pin" : str(self.pin),
                                 'sedzia': self.nazwaSedziego, 'kolor': self.color, 'glosNaTak' : self.glosNaTak
                                 }, namespace='/test'
                      )

# Tworzymy guziki - reprezentacja fizycznych guzikow w pamieci komputera
# Piny na głos TAK- 11, 13, 15
# Piny na głos NIE-  29, 31, 33
przycisk1naTak = Przycisk(11, GPIO.IN, "KendzioR", "green", True)
przycisk1naNie = Przycisk(29, GPIO.IN, "KendzioR", "red", False)
przycisk2naTak = Przycisk(13, GPIO.IN, "FurmanS", "green", True)
przycisk2naNie = Przycisk(31, GPIO.IN, "FurmanS", "red", False)
przycisk3naTak = Przycisk(15, GPIO.IN, "Zorro", "green", True)
przycisk3naNie = Przycisk(33, GPIO.IN, "Zorro", "red", False)
# Lista wszystkich przyciskow
listaPrzyciskow = [przycisk1naTak, przycisk1naNie, przycisk2naTak, przycisk2naNie, przycisk3naTak, przycisk3naNie]

#print "Przyciski zainicjalizowane w systemie: "
#for index, pojedynczyPrzycisk in enumerate(listaPrzyciskow):

@socketio.on('my event', namespace='/test')
def my_event(msg):
    print( msg['data'])

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
