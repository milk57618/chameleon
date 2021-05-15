import time
import Adafruit_DHT
from datetime import datetime


class Monitor():
    def __init__(self):
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 4
        self.POS = "TH01"
    
    def getHumidTemp():
        h,t = Adafruit_DHT.read_retry(self.DHT_SENSOR,self.DHT_PIN)
        return h,t