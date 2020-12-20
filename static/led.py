import sys;
import RPi.GPIO as GPIO
import time
import threading

if sys.version_info[0]>2: #Just making sure the program works with both Python 2.x and 3.x
    from queue import Queue
else:
    from Queue import Queue

GPIO.setmode(GPIO.BOARD) # sprawdz co znaczy BCM

class Przycisk:
    def __init__(self, pin, trybGPIO, nazwaSedziego, colorPrzycisku):
        self.config = GPIO.setup(pin, trybGPIO, pull_up_down=GPIO.PUD_UP)
        self.pin = pin
        self.tryp = trybGPIO
        self.nazwaSedziego = nazwaSedziego
        self.color = colorPrzycisku
        GPIO.add_event_detect(self.pin, GPIO.FALLING, callback=self.odbierzZmianeStanu, bouncetime=400)

    def odbierzZmianeStanu(self, channel):
        print "Glos od sedziego " + self.nazwaSedziego + " odebrany na przycisku o PIN " + str(self.pin)

przycisk1 = Przycisk(19, GPIO.IN, "KendzioR", "Niebieski")
przycisk2 = Przycisk(23, GPIO.IN, "FurmanS", "Zolty")
przycisk3 = Przycisk(24, GPIO.IN, "Zorro", "Czarny")
listaPrzyciskow = [przycisk1, przycisk2, przycisk3]

print "Przyciski zainicjalizowane w systemie: " 
for index, pojedynczyPrzycisk in enumerate(listaPrzyciskow):
    print str(index) + ". Nazwa Sedziego " + pojedynczyPrzycisk.nazwaSedziego + " Pin Sedziego " + str(pojedynczyPrzycisk.pin)

print "Nasluchuje przyciski na pinach 19, 23, 24"

while True:
     time.sleep(0.2)
